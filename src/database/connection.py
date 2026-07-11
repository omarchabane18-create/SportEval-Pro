"""
Database connection module
"""

import logging
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from src.config import CONFIG

logger = logging.getLogger(__name__)


class Database:
    """Singleton database connection manager"""
    
    _instance = None
    _engine = None
    _session_factory = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_instance():
        """Get or create database instance"""
        if Database._instance is None:
            Database._instance = Database()
        return Database._instance
    
    def connect(self):
        """Create database engine and session factory"""
        try:
            # Create engine
            self._engine = create_engine(
                CONFIG.DATABASE_URL,
                echo=CONFIG.DEBUG,
                connect_args={"check_same_thread": False} if "sqlite" in CONFIG.DATABASE_URL else {}
            )
            
            # Enable foreign keys for SQLite
            if "sqlite" in CONFIG.DATABASE_URL:
                @event.listens_for(self._engine, "connect")
                def set_sqlite_pragma(dbapi_conn, connection_record):
                    cursor = dbapi_conn.cursor()
                    cursor.execute("PRAGMA foreign_keys=ON")
                    cursor.close()
            
            # Create session factory
            self._session_factory = sessionmaker(bind=self._engine)
            
            logger.info(f"✅ Connected to database: {CONFIG.DATABASE_URL}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to connect to database: {e}")
            raise
    
    def get_session(self) -> Session:
        """Get a new database session"""
        if self._session_factory is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        return self._session_factory()
    
    def create_all_tables(self):
        """Create all tables"""
        if self._engine is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        
        from src.database.models import Base
        Base.metadata.create_all(self._engine)
        logger.info("✅ Database tables created")
    
    def drop_all_tables(self):
        """Drop all tables (use with caution)"""
        if self._engine is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        
        from src.database.models import Base
        Base.metadata.drop_all(self._engine)
        logger.info("⚠️ All database tables dropped")
    
    def close(self):
        """Close database connection"""
        if self._engine:
            self._engine.dispose()
            logger.info("🔌 Database connection closed")


# Context manager for sessions
class SessionContextManager:
    """Context manager for database sessions"""
    
    def __init__(self):
        self.session = None
    
    def __enter__(self):
        self.session = Database.get_instance().get_session()
        return self.session
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()


def get_session():
    """Dependency injection for sessions"""
    return SessionContextManager()
