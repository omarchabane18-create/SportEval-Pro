"""
Database setup and initialization script
"""

import logging
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.database.connection import Database
from src.database.models import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_database():
    """Initialize the database"""
    try:
        logger.info("🔧 Setting up database...")
        
        # Connect to database
        db = Database.get_instance()
        db.connect()
        
        # Create all tables
        db.create_all_tables()
        
        logger.info("✅ Database setup completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error setting up database: {e}", exc_info=True)
        return False


if __name__ == "__main__":
    success = setup_database()
    sys.exit(0 if success else 1)
