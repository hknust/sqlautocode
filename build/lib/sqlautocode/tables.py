# -*- coding: utf-8 -*-
## File autogenerated by SQLAutoCode
## see http://code.google.com/p/sqlautocode/

from sqlalchemy import *
from sqlalchemy.dialects.mysql import *

metadata = MetaData()


ITSD = Table('ITSD', metadata,*[
    Column('ITSDId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('ReportingCode', VARCHAR(length=20), primary_key=False),
    Column('FirstName', VARCHAR(length=100), primary_key=False),
    Column('LastName', VARCHAR(length=100), primary_key=False),
    Column('WorkerNumber', VARCHAR(length=20), primary_key=False),
    Column('TicketNumber', VARCHAR(length=30), primary_key=False),
    Column('FindingsText', VARCHAR(length=1000), primary_key=False),
    Column('SerialNumber', VARCHAR(length=100), primary_key=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),
    Column('CreateTimestamp', DATETIME(), primary_key=False, nullable=False),
    Column('CreateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('eSketchTimestamp', DATETIME(), primary_key=False),
    Column('QManagerTimestamp', DATETIME(), primary_key=False),
    Column('ITSDTimestamp', DATETIME(), primary_key=False),
    Column('ActiveRowFlag', TINYINT(display_width=4), primary_key=False, nullable=False),
    Column('RowActiveDate', DATETIME(), primary_key=False, nullable=False),
    Column('RowInactiveDate', DATETIME(), primary_key=False),
    Column('TicketId', VARCHAR(length=30), primary_key=False),])


NotificationLog = Table('NotificationLog', metadata,*[
    Column('NotificationLogId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('SubscriberXML', MEDIUMTEXT(), primary_key=False),
    Column('SubscriptionId', BIGINT(display_width=20), primary_key=False, nullable=False),
    Column('SentTimestamp', DATETIME(), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])
Index('FK1_NotificationLog_Subscription', NotificationLog.c.SubscriptionId, unique=False)


Object = Table('Object', metadata,*[
    Column('ObjectId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('ParentObjectId', BIGINT(display_width=20), primary_key=False),
    Column('Name', VARCHAR(length=1000), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])
Index('FK1_Object_Object', Object.c.ParentObjectId, unique=False)


Operation = Table('Operation', metadata,*[
    Column('OperationId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('Value', VARCHAR(length=5000), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])


Permission = Table('Permission', metadata,*[
    Column('PermissionId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('ObjectId', BIGINT(display_width=20), primary_key=False, nullable=False),
    Column('OperationId', BIGINT(display_width=20), primary_key=False, nullable=False),
    Column('Name', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])
Index('FK1_Permission_Operation', Permission.c.OperationId, unique=False)
Index('FK1_Permission_Object', Permission.c.ObjectId, unique=False)


Role = Table('Role', metadata,*[
    Column('RoleId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('Name', VARCHAR(length=100), primary_key=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])


RolePermission = Table('RolePermission', metadata,*[
    Column('PermissionId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('RoleId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('AuditFlag', TINYINT(display_width=4), primary_key=False, nullable=False, default=text("'0'")),
    Column('NotificationFlag', TINYINT(display_width=4), primary_key=False, nullable=False, default=text("'0'")),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])
Index('FK1_RolePermission_Role', RolePermission.c.RoleId, unique=False)


Subscription = Table('Subscription', metadata,*[
    Column('SubscriptionId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('SubscriptionName', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('SubscriptionDescription', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('ActiveFlag', BIT(length=1), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])
Index('XAK1Subscription', Subscription.c.SubscriptionName, unique=True)


SubscriptionSystemUser = Table('SubscriptionSystemUser', metadata,*[
    Column('SubscriptionId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('SystemUserId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])
Index('FK1_Subscription_SystemUser', SubscriptionSystemUser.c.SystemUserId, unique=False)


SystemUser = Table('SystemUser', metadata,*[
    Column('SystemUserId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('CurrentToken', VARCHAR(length=100), primary_key=False),
    Column('CurrentTokenTimestamp', DATETIME(), primary_key=False),
    Column('EmailAddressText', VARCHAR(length=255), primary_key=False),
    Column('LoginUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),])


SystemUserRole = Table('SystemUserRole', metadata,*[
    Column('SystemUserRoleId', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('RoleId', BIGINT(display_width=20), primary_key=False, nullable=False),
    Column('SystemUserId', BIGINT(display_width=20), primary_key=False, nullable=False),
    Column('LastUpdateUserId', VARCHAR(length=100), primary_key=False, nullable=False),
    Column('LastUpdateTimestamp', DATETIME(), primary_key=False, nullable=False),
    Column('ActiveFlag', TINYINT(display_width=4), primary_key=False, nullable=False),])
Index('FK1_SystemUserRole_SystemUser', SystemUserRole.c.SystemUserId, unique=False)
Index('XAK1SystemUserRole', SystemUserRole.c.RoleId, SystemUserRole.c.SystemUserId, unique=True)

