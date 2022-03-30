import sqlalchemy as sql 
import sqlalchemy.orm as orm 
import sqlalchemy as sql 
import sqlalchemy.ext.declarative as declarative 
import sqlalchemy.orm as orm 
import database 
from sqlalchemy.sql import func

'''
DATABASE SCHEMA

'''

class SubscriptionType(database.Base):

    __tablename__ = 'subscriptiontype'

    subscriptiontypeid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.String,nullable=False)

class Day(database.Base):

    __tablename__ = 'day'

    dayid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.String,nullable=False)
    openingschedule = orm.relationship('OpeningSchedule',backref='day')

class Users(database.Base):

    __tablename__ = 'users'

    usersid = sql.Column(sql.Integer,primary_key=True,index=True)
    firstname = sql.Column(sql.String,nullable=False)
    lastname = sql.Column(sql.String,nullable=False)
    email = sql.Column(sql.String,nullable=False)
    dateofbirth = sql.Column(sql.Date,nullable=False)
    address = sql.Column(sql.String,nullable=False)
    password = sql.Column(sql.String,nullable=False)
    paymentstatus = sql.Column(sql.Boolean,nullable=False)
    subscriptiontypeid = sql.Column(sql.Integer,sql.ForeignKey('subscriptiontype.subscriptiontypeid'))


    transaction = orm.relationship('Transaction',backref='users')

class Branch(database.Base):

    __tablename__ = 'branch'

    branchid = sql.Column(sql.Integer,primary_key=True,index=True)
    name = sql.Column(sql.String,nullable=False)
    anb = sql.Column(sql.BigInteger,nullable=False)
    address = sql.Column(sql.String,nullable=False)
    state = sql.Column(sql.String,nullable=False)
    postcode = sql.Column(sql.Integer,nullable=False)
    branchopeningschedule = orm.relationship('BranchOpeningSchedule',backref='branch')
    branchmenu = orm.relationship('BranchMenu',backref='branch')

class OpeningSchedule(database.Base):

    __tablename__ = 'openingschedule'

    openingscheduleid= sql.Column(sql.Integer,primary_key=True,index=True)
    dayid = sql.Column(sql.Integer, sql.ForeignKey('day.dayid'))
    openingtime = sql.Column(sql.Time,nullable=False)
    closingtime = sql.Column(sql.Time,nullable=False)

    branchopeningschedule = orm.relationship('BranchOpeningSchedule',backref='openingschedule')

class BranchOpeningSchedule(database.Base):

    __tablename__ = 'branchopeningschedule'

    branchopeningscheduleid = sql.Column(sql.Integer,primary_key=True,nullable=False)
    branchid = sql.Column(sql.Integer,sql.ForeignKey('branch.branchid'))
    openingscheduleid = sql.Column(sql.Integer,sql.ForeignKey('openingschedule.openingscheduleid'))

class BranchMenu(database.Base):

    __tablename__ = 'branchmenu'

    branchmenuid = sql.Column(sql.Integer,primary_key=True,index=True)
    branchid = sql.Column(sql.Integer,sql.ForeignKey('branch.branchid'))
    description = sql.Column(sql.String,nullable=False)
    pictureurl = sql.Column(sql.String)
    submittedtime = sql.Column(sql.TIMESTAMP,server_default=func.now(),onupdate=func.current_timestamp())
    active = sql.Column(sql.Boolean,nullable=False)
    transaction = orm.relationship('Transaction',backref='branchmenu')
    branchmenutag = orm.relationship('BranchMenuTag',backref='branchmenu')

class Transaction(database.Base):

    __tablename__ = 'transaction'

    transactionid =  sql.Column(sql.Integer,primary_key=True,index=True)
    usersid = sql.Column(sql.Integer,sql.ForeignKey('users.usersid'))
    branchmenuid = sql.Column(sql.Integer,sql.ForeignKey('branchmenu.branchmenuid'))
    collected = sql.Column(sql.Boolean,nullable=False)
    collectedtime = sql.Column(sql.Time)

class Tag(database.Base):

    __tablename__ = 'tag'

    tagid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.String,nullable=False)
    tagurl = sql.Column(sql.String)

    branchmenutag = orm.relationship('BranchMenuTag',backref='tag')

class BranchMenuTag(database.Base):

    __tablename__ = 'branchmenutag'

    branchmenutagid =sql.Column(sql.Integer,primary_key=True,index=True)
    branchmenuid = sql.Column(sql.Integer,sql.ForeignKey('branchmenu.branchmenuid'))
    tagid = sql.Column(sql.Integer,sql.ForeignKey('tag.tagid'))
