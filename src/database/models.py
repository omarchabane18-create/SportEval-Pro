"""
SQLAlchemy models for SportEval Pro
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Establishment(Base):
    """Establishment (École/Lycée) model"""
    __tablename__ = "establishments"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    address = Column(String(255))
    city = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100), unique=True)
    director_name = Column(String(255))
    director_email = Column(String(100))
    massar_code = Column(String(50), unique=True)  # Ministry code
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    teachers = relationship("Teacher", back_populates="establishment", cascade="all, delete-orphan")
    classes = relationship("Class", back_populates="establishment", cascade="all, delete-orphan")
    students = relationship("Student", back_populates="establishment", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Establishment(id={self.id}, name='{self.name}')>"


class Teacher(Base):
    """Teacher (Enseignant EPS) model"""
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    specialty = Column(String(100))  # EPS specialty
    cin = Column(String(50), unique=True)  # National ID
    signature_url = Column(String(255))  # Path to signature image
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    establishment = relationship("Establishment", back_populates="teachers")
    classes = relationship("Class", back_populates="teacher")
    evaluations = relationship("Evaluation", back_populates="teacher")
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.first_name} {self.last_name}')>"


class Class(Base):
    """Class (Classe) model"""
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)  # e.g., "1ère S", "2nde"
    level = Column(String(50))  # Academic level
    year = Column(Integer)  # School year
    section = Column(String(50))  # Section (S, L, STG, etc.)
    max_students = Column(Integer, default=50)
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    establishment = relationship("Establishment", back_populates="classes")
    teacher = relationship("Teacher", back_populates="classes")
    students = relationship("Student", back_populates="class_", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Class(id={self.id}, name='{self.name}')>"


class Student(Base):
    """Student (Élève) model"""
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    gender = Column(String(10))  # M, F
    birth_date = Column(DateTime)
    height = Column(Float)  # cm
    weight = Column(Float)  # kg
    massar_code = Column(String(50), unique=True)  # National ID
    photo_url = Column(String(255))
    medical_notes = Column(Text)  # Optional medical information
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    class_ = relationship("Class", back_populates="students")
    establishment = relationship("Establishment", back_populates="students")
    evaluations = relationship("Evaluation", back_populates="student", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}')>"
    
    @property
    def age(self):
        """Calculate age"""
        if self.birth_date:
            today = datetime.utcnow()
            return today.year - self.birth_date.year
        return None
    
    @property
    def bmi(self):
        """Calculate BMI"""
        if self.height and self.weight:
            height_m = self.height / 100
            return self.weight / (height_m ** 2)
        return None


class Event(Base):
    """Event/Test (Épreuve) model"""
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)  # e.g., "100m", "Saut en longueur"
    category = Column(String(50))  # Athlétisme, Sports collectifs, Gymnastique
    event_type = Column(String(50))  # Course, Saut, Lancer, Collectif, Gymnastique
    unit = Column(String(50))  # m, s, cm, points, etc.
    gender = Column(String(10))  # M, F, Mixed
    level = Column(String(50))  # 1ère, 2nde, etc.
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    evaluations = relationship("Evaluation", back_populates="event", cascade="all, delete-orphan")
    benchmarks = relationship("Benchmark", back_populates="event", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Event(id={self.id}, name='{self.name}')>"


class Benchmark(Base):
    """Benchmark (Barème) model - Official Moroccan standards"""
    __tablename__ = "benchmarks"
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    gender = Column(String(10))  # M, F
    age_min = Column(Integer)
    age_max = Column(Integer)
    grade_a_min = Column(Float)  # Grade A threshold
    grade_b_min = Column(Float)  # Grade B threshold
    grade_c_min = Column(Float)  # Grade C threshold
    grade_d_min = Column(Float)  # Grade D threshold
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    event = relationship("Event", back_populates="benchmarks")
    
    def __repr__(self):
        return f"<Benchmark(id={self.id}, event_id={self.event_id})>"


class Evaluation(Base):
    """Evaluation (Résultat d'évaluation) model"""
    __tablename__ = "evaluations"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    raw_score = Column(Float, nullable=False)  # Raw score value
    grade = Column(String(2))  # A, B, C, D, F
    ranking = Column(Integer)  # Position in class
    percentile = Column(Float)  # Percentile in class
    notes = Column(Text)  # Teacher notes
    evaluation_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    student = relationship("Student", back_populates="evaluations")
    event = relationship("Event", back_populates="evaluations")
    teacher = relationship("Teacher", back_populates="evaluations")
    spas_scores = relationship("SPASScore", back_populates="evaluation", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Evaluation(id={self.id}, student_id={self.student_id}, event_id={self.event_id})>"


class SPASScore(Base):
    """SPAS Engine Calculated Scores model"""
    __tablename__ = "spas_scores"
    
    id = Column(Integer, primary_key=True)
    evaluation_id = Column(Integer, ForeignKey("evaluations.id"), nullable=False)
    mpi = Column(Float)  # Morphological Performance Index
    ssi = Column(Float)  # Speed Score Index
    epi = Column(Float)  # Explosive Power Index
    esi = Column(Float)  # Endurance Score Index
    api = Column(Float)  # Athletic Potential Index
    gpi = Column(Float)  # Global Performance Index
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    evaluation = relationship("Evaluation", back_populates="spas_scores")
    
    def __repr__(self):
        return f"<SPASScore(id={self.id}, gpi={self.gpi})>"


class AuditLog(Base):
    """Audit log for tracking changes"""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True)
    table_name = Column(String(100), nullable=False)
    record_id = Column(Integer)
    action = Column(String(50), nullable=False)  # CREATE, UPDATE, DELETE
    old_value = Column(Text)
    new_value = Column(Text)
    user_id = Column(Integer)  # User who made the change
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<AuditLog(id={self.id}, action='{self.action}', table='{self.table_name}')>"
