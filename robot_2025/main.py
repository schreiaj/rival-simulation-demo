#!/usr/bin/env python3
"""
Main entry point for the 2025_robot project.
"""

import sys
import os
import yaml
import time
import signal

# Add the current directory to the Python path to help with imports
# This is needed because we're importing hello_world_node.py directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from tide.core.utils import launch_from_config


def main():
    """Launch nodes from configuration."""
    # Load configuration
    config_path = "config/config.yaml"
    print(f"Loading configuration from {config_path}")
    
    nodes = []  # Initialize nodes list
    shutdown_in_progress = False
    
    # Define shutdown handler to ensure clean exit
    def shutdown_handler(sig=None, frame=None):
        nonlocal shutdown_in_progress
        
        # Prevent multiple calls to shutdown
        if shutdown_in_progress:
            return
            
        shutdown_in_progress = True
        print("\nShutting down...")
        
        # Stop all nodes
        for node in nodes:
            try:
                node.stop()
            except Exception as e:
                # Just log errors during shutdown
                pass
                
        print("Nodes stopped")
        sys.exit(0)
    
    try:
        # Load configuration
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        
        # Make sure hello_world_node can be imported directly
        try:
            # Try to import to check if it's available
            import hello_world_node
            print("Found hello_world_node module")
        except ImportError as e:
            print(f"Warning: {e}. Make sure hello_world_node.py is in the current directory.")
        
        # Launch nodes from config
        nodes = launch_from_config(config)
        
        print(f"Started {len(nodes)} nodes. Press Ctrl+C to exit.")
        
        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, shutdown_handler)
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    finally:
        # Ensure cleanup happens even on unexpected errors
        if not shutdown_in_progress:
            shutdown_handler()
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 