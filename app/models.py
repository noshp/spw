from app import db, app


class UniversityEmploymentRates(db.Model):
    __tablename__ = 'university-employment-rates'
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class UniversityProgramList(db.Model):
    __tablename__ = 'university_program_list'
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class NOCSynonymList(db.Model):
    __tablename__ = 'noc_synonym_list'
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class NOCList(db.Model):
    __tablename__ = "noc_list"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class SkillLevelList(db.Model):
    __tablename__ = "skilllevel_list"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class TaskList(db.Model):
    __tablename__ = "task_list"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }
class EssentialSkills(db.Model):
    __tablename__ = "essential-skills"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class TotalJobOpenings(db.Model):
    __tablename__ = "totaljobopenings"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class NOCLocationList(db.Model):
    __tablename__ = "noc_location_list"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }

class NOCSalaryList(db.Model):
    __tablename__ = "noc_salary_list"
    __table_args__ = {
        'autoload': True,
        'schema': 'public',
        'autoload_with': db.engine
    }