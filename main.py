#!/usr/bin/env python3
"""
Digital Scrabble Game
Main entry point

This module initializes and runs the Scrabble game application.
"""

import sys
import os
from PyQt5.QtWidgets import QApplication

from controllers.game_controller import GameController

def main():
    """Main entry point for the application."""
    # Create resources directory if it doesn't exist
    os.makedirs('resources', exist_ok=True)
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Digital Scrabble")
    
    # Create and show controller
    controller = GameController()
    controller.show()
    
    # Run application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 