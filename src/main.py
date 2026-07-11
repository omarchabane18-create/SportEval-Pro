"""
SportEval Pro - Main Entry Point
Version: 1.0.0
"""

import sys
import logging
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config import Config
from src.database.connection import Database

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main entry point for SportEval Pro"""
    logger.info("🏃 SportEval Pro - Starting...")
    
    try:
        # Initialize database
        db = Database.get_instance()
        db.connect()
        logger.info("✅ Database initialized")
        
        # TODO: Import UI classes
        # from src.ui.main_window import MainWindow
        # app = MainWindow()
        # app.show()
        
        logger.info("✅ Application started successfully")
        print("\n" + "="*50)
        print("🏃 SportEval Pro - AI-Powered EPS Assessment")
        print("="*50)
        print("\n✨ Welcome! The application is ready to use.")
        print("📖 For more info, check: https://github.com/omarchabane18-create/SportEval-Pro")
        print("\n")
        
    except Exception as e:
        logger.error(f"❌ Error starting application: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
