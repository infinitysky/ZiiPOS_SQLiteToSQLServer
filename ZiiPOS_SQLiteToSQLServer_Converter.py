import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import sys
import os
import pandas as pd
import sqlite3
import numpy as np
import xlsxwriter
import xlrd
import ssl
import re 
import pyodbc

from tqdm import tqdm


ssl._create_default_https_context = ssl._create_unverified_context

#Global Value
directory='C:\\Ziitech\\SQL'
# createSQLFileCheckFlag=1
# createExcelFileCheckFlag=1

SingleSqlFile = directory + "\\00_Settings.sql"


def initSingleSQLFile():
    fileName = SingleSqlFile
    if os.path.exists(fileName):
            os.remove(fileName)
        
    dbsqlquery=open(fileName,'w')
    dbsqlquery.write(r''' 

-- ALTER DATABASE CURRENT COLLATE Chinese_PRC_CI_AS;
                                
EXEC sp_MSforeachtable @command1="ALTER TABLE ? DISABLE TRIGGER ALL;"
                     

IF COL_LENGTH('AccessMenu', 'PId') IS NOT NULL
  dbcc checkident(AccessMenu,reseed,1000000)
ELSE  
  alter table AccessMenu add PId bigint identity(1000000,1);

IF COL_LENGTH('Attendance', 'PId') IS NOT NULL
  dbcc checkident(Attendance,reseed,1000000)
ELSE  
  alter table Attendance add PId bigint identity(1000000,1);

IF COL_LENGTH('BankHead', 'PId') IS NOT NULL
  dbcc checkident(BankHead,reseed,1000000)
ELSE  
  alter table BankHead add PId bigint identity(1000000,1);

IF COL_LENGTH('BankTransaction', 'PId') IS NOT NULL
  dbcc checkident(BankTransaction,reseed,1000000)
ELSE  
  alter table BankTransaction add PId bigint identity(1000000,1);

IF COL_LENGTH('BookDetail', 'PId') IS NOT NULL
  dbcc checkident(BookDetail,reseed,1000000)
ELSE  
  alter table BookDetail add PId bigint identity(1000000,1);

IF COL_LENGTH('BookTable', 'PId') IS NOT NULL
  dbcc checkident(BookTable,reseed,1000000)
ELSE  
  alter table BookTable add PId bigint identity(1000000,1);

IF COL_LENGTH('ButtonsTable', 'PId') IS NOT NULL
  dbcc checkident(ButtonsTable,reseed,1000000)
ELSE  
  alter table ButtonsTable add PId bigint identity(1000000,1);

IF COL_LENGTH('CancelSalesHead', 'PId') IS NOT NULL
  dbcc checkident(CancelSalesHead,reseed,1000000)
ELSE  
  alter table CancelSalesHead add PId bigint identity(1000000,1);

IF COL_LENGTH('CancelSalesItem', 'PId') IS NOT NULL
  dbcc checkident(CancelSalesItem,reseed,1000000)
ELSE  
  alter table CancelSalesItem add PId bigint identity(1000000,1);

IF COL_LENGTH('CashDeclaration', 'PId') IS NOT NULL
  dbcc checkident(CashDeclaration,reseed,1000000)
ELSE  
  alter table CashDeclaration add PId bigint identity(1000000,1);

IF COL_LENGTH('CashFloatTable', 'PId') IS NOT NULL
  dbcc checkident(CashFloatTable,reseed,1000000)
ELSE  
  alter table CashFloatTable add PId bigint identity(1000000,1);

IF COL_LENGTH('Category', 'PId') IS NOT NULL
  dbcc checkident(Category,reseed,1000000)
ELSE  
  alter table Category add PId bigint identity(1000000,1);

IF COL_LENGTH('CategoryMenuItem', 'PId') IS NOT NULL
  dbcc checkident(CategoryMenuItem,reseed,1000000)
ELSE  
  alter table CategoryMenuItem add PId bigint identity(1000000,1);

IF COL_LENGTH('ChannelPaymentActivity', 'PId') IS NOT NULL
  dbcc checkident(ChannelPaymentActivity,reseed,1000000)
ELSE  
  alter table ChannelPaymentActivity add PId bigint identity(1000000,1);

IF COL_LENGTH('ChargeScope', 'PId') IS NOT NULL
  dbcc checkident(ChargeScope,reseed,1000000)
ELSE  
  alter table ChargeScope add PId bigint identity(1000000,1);

IF COL_LENGTH('Chart', 'PId') IS NOT NULL
  dbcc checkident(Chart,reseed,1000000)
ELSE  
  alter table Chart add PId bigint identity(1000000,1);

IF COL_LENGTH('CloudMenuPicture', 'PId') IS NOT NULL
  dbcc checkident(CloudMenuPicture,reseed,1000000)
ELSE  
  alter table CloudMenuPicture add PId bigint identity(1000000,1);

IF COL_LENGTH('CloudMenuSync', 'PId') IS NOT NULL
  dbcc checkident(CloudMenuSync,reseed,1000000)
ELSE  
  alter table CloudMenuSync add PId bigint identity(1000000,1);

IF COL_LENGTH('CloudMenuVersion', 'PId') IS NOT NULL
  dbcc checkident(CloudMenuVersion,reseed,1000000)
ELSE  
  alter table CloudMenuVersion add PId bigint identity(1000000,1);


IF COL_LENGTH('course', 'PId') IS NOT NULL
  dbcc checkident(course,reseed,1000000)
ELSE  
  alter table course add PId bigint identity(1000000,1);

IF COL_LENGTH('DBVersion', 'PId') IS NOT NULL
  dbcc checkident(DBVersion,reseed,1000000)
ELSE  
  alter table DBVersion add PId bigint identity(1000000,1);

IF COL_LENGTH('DefaultMenuDeal', 'PId') IS NOT NULL
  dbcc checkident(DefaultMenuDeal,reseed,1000000)
ELSE  
  alter table DefaultMenuDeal add PId bigint identity(1000000,1);

IF COL_LENGTH('DepositTable', 'PId') IS NOT NULL
  dbcc checkident(DepositTable,reseed,1000000)
ELSE  
  alter table DepositTable add PId bigint identity(1000000,1);

IF COL_LENGTH('DiscountRateTable', 'PId') IS NOT NULL
  dbcc checkident(DiscountRateTable,reseed,1000000)
ELSE  
  alter table DiscountRateTable add PId bigint identity(1000000,1);


IF COL_LENGTH('DrawerDevice', 'PId') IS NOT NULL
  dbcc checkident(DrawerDevice,reseed,1000000)
ELSE  
  alter table DrawerDevice add PId bigint identity(1000000,1);


IF COL_LENGTH('DrawerOpenRecordTable', 'PId') IS NOT NULL
  dbcc checkident(DrawerOpenRecordTable,reseed,1000000)
ELSE  
  alter table DrawerOpenRecordTable add PId bigint identity(1000000,1);

IF COL_LENGTH('EftLog', 'PId') IS NOT NULL
  dbcc checkident(EftLog,reseed,1000000)
ELSE  
  alter table EftLog add PId bigint identity(1000000,1);

IF COL_LENGTH('EftMachinePair', 'PId') IS NOT NULL
  dbcc checkident(EftMachinePair,reseed,1000000)
ELSE  
  alter table EftMachinePair add PId bigint identity(1000000,1);

IF COL_LENGTH('EftMerReceipt', 'PId') IS NOT NULL
  dbcc checkident(EftMerReceipt,reseed,1000000)
ELSE  
  alter table EftMerReceipt add PId bigint identity(1000000,1);

IF COL_LENGTH('EftSettlement', 'PId') IS NOT NULL
  dbcc checkident(EftSettlement,reseed,1000000)
ELSE  
  alter table EftSettlement add PId bigint identity(1000000,1);

IF COL_LENGTH('EftTransactionActive', 'PId') IS NOT NULL
  dbcc checkident(EftTransactionActive,reseed,1000000)
ELSE  
  alter table EftTransactionActive add PId bigint identity(1000000,1);

IF COL_LENGTH('ExpAcct', 'PId') IS NOT NULL
  dbcc checkident(ExpAcct,reseed,1000000)
ELSE  
  alter table ExpAcct add PId bigint identity(1000000,1);

IF COL_LENGTH('ExpDetail', 'PId') IS NOT NULL
  dbcc checkident(ExpDetail,reseed,1000000)
ELSE  
  alter table ExpDetail add PId bigint identity(1000000,1);

IF COL_LENGTH('Expenses', 'PId') IS NOT NULL
  dbcc checkident(Expenses,reseed,1000000)
ELSE  
  alter table Expenses add PId bigint identity(1000000,1);

IF COL_LENGTH('GiftCardSales', 'PId') IS NOT NULL
  dbcc checkident(GiftCardSales,reseed,1000000)
ELSE  
  alter table GiftCardSales add PId bigint identity(1000000,1);

IF COL_LENGTH('HoldHead', 'PId') IS NOT NULL
  dbcc checkident(HoldHead,reseed,1000000)
ELSE  
  alter table HoldHead add PId bigint identity(1000000,1);

IF COL_LENGTH('HoldItem', 'PId') IS NOT NULL
  dbcc checkident(HoldItem,reseed,1000000)
ELSE  
  alter table HoldItem add PId bigint identity(1000000,1);

IF COL_LENGTH('HolidayTable', 'PId') IS NOT NULL
  dbcc checkident(HolidayTable,reseed,1000000)
ELSE  
  alter table HolidayTable add PId bigint identity(1000000,1);

IF COL_LENGTH('IngredientsTable', 'PId') IS NOT NULL
  dbcc checkident(IngredientsTable,reseed,1000000)
ELSE  
  alter table IngredientsTable add PId bigint identity(1000000,1);


IF COL_LENGTH('InstructionLink', 'PId') IS NOT NULL
  dbcc checkident(InstructionLink,reseed,1000000)
ELSE  
  alter table InstructionLink add PId bigint identity(1000000,1);

IF COL_LENGTH('InstructionLinkGroup', 'PId') IS NOT NULL
  dbcc checkident(InstructionLinkGroup,reseed,1000000)
ELSE  
  alter table InstructionLinkGroup add PId bigint identity(1000000,1);

IF COL_LENGTH('IPPermission', 'PId') IS NOT NULL
  dbcc checkident(IPPermission,reseed,1000000)
ELSE  
  alter table IPPermission add PId bigint identity(1000000,1);

IF COL_LENGTH('ItemGroupTable', 'PId') IS NOT NULL
  dbcc checkident(ItemGroupTable,reseed,1000000)
ELSE  
  alter table ItemGroupTable add PId bigint identity(1000000,1);


IF COL_LENGTH('KitchenScreen', 'PId') IS NOT NULL
  dbcc checkident(KitchenScreen,reseed,1000000)
ELSE  
  alter table KitchenScreen add PId bigint identity(1000000,1);

IF COL_LENGTH('LoyaltyPoints', 'PId') IS NOT NULL
  dbcc checkident(LoyaltyPoints,reseed,1000000)
ELSE  
  alter table LoyaltyPoints add PId bigint identity(1000000,1);

IF COL_LENGTH('MachineID', 'PId') IS NOT NULL
  dbcc checkident(MachineID,reseed,1000000)
ELSE  
  alter table MachineID add PId bigint identity(1000000,1);



IF COL_LENGTH('MealPackage', 'PId') IS NOT NULL
  dbcc checkident(MealPackage,reseed,1000000)
ELSE  
  alter table MealPackage add PId bigint identity(1000000,1);

IF COL_LENGTH('Menu', 'PId') IS NOT NULL
  dbcc checkident(Menu,reseed,1000000)
ELSE  
  alter table Menu add PId bigint identity(1000000,1);

IF COL_LENGTH('MenuGroupLinkCategory', 'PId') IS NOT NULL
  dbcc checkident(MenuGroupLinkCategory,reseed,1000000)
ELSE  
  alter table MenuGroupLinkCategory add PId bigint identity(1000000,1);

IF COL_LENGTH('MenuGroupTable', 'PId') IS NOT NULL
  dbcc checkident(MenuGroupTable,reseed,1000000)
ELSE  
  alter table MenuGroupTable add PId bigint identity(1000000,1);

IF COL_LENGTH('MenuGroupTimes', 'PId') IS NOT NULL
  dbcc checkident(MenuGroupTimes,reseed,1000000)
ELSE  
  alter table MenuGroupTimes add PId bigint identity(1000000,1);

IF COL_LENGTH('MenuItem', 'PId') IS NOT NULL
  dbcc checkident(MenuItem,reseed,1000000)
ELSE  
  alter table MenuItem add PId bigint identity(1000000,1);

IF COL_LENGTH('MenuItemRelation', 'PId') IS NOT NULL
  dbcc checkident(MenuItemRelation,reseed,1000000)
ELSE  
  alter table MenuItemRelation add PId bigint identity(1000000,1);

IF COL_LENGTH('MenuSyncLog', 'PId') IS NOT NULL
  dbcc checkident(MenuSyncLog,reseed,1000000)
ELSE  
  alter table MenuSyncLog add PId bigint identity(1000000,1);

IF COL_LENGTH('messi', 'PId') IS NOT NULL
  dbcc checkident(messi,reseed,1000000)
ELSE  
  alter table messi add PId bigint identity(1000000,1);


IF COL_LENGTH('OnlineOrderReceiver', 'PId') IS NOT NULL
  dbcc checkident(OnlineOrderReceiver,reseed,1000000)
ELSE  
  alter table OnlineOrderReceiver add PId bigint identity(1000000,1);



IF COL_LENGTH('OrderH', 'PId') IS NOT NULL
  dbcc checkident(OrderH,reseed,1000000)
ELSE  
  alter table OrderH add PId bigint identity(1000000,1);

IF COL_LENGTH('OrderI', 'PId') IS NOT NULL
  dbcc checkident(OrderI,reseed,1000000)
ELSE  
  alter table OrderI add PId bigint identity(1000000,1);

IF COL_LENGTH('OrderOpRecord', 'PId') IS NOT NULL
  dbcc checkident(OrderOpRecord,reseed,1000000)
ELSE  
  alter table OrderOpRecord add PId bigint identity(1000000,1);


IF COL_LENGTH('PayAcct', 'PId') IS NOT NULL
  dbcc checkident(PayAcct,reseed,1000000)
ELSE  
  alter table PayAcct add PId bigint identity(1000000,1);

IF COL_LENGTH('Payment', 'PId') IS NOT NULL
  dbcc checkident(Payment,reseed,1000000)
ELSE  
  alter table Payment add PId bigint identity(1000000,1);

IF COL_LENGTH('PayOutTable', 'PId') IS NOT NULL
  dbcc checkident(PayOutTable,reseed,1000000)
ELSE  
  alter table PayOutTable add PId bigint identity(1000000,1);

IF COL_LENGTH('PictureMeta', 'PId') IS NOT NULL
  dbcc checkident(PictureMeta,reseed,1000000)
ELSE  
  alter table PictureMeta add PId bigint identity(1000000,1);

IF COL_LENGTH('PresetNote', 'PId') IS NOT NULL
  dbcc checkident(PresetNote,reseed,1000000)
ELSE  
  alter table PresetNote add PId bigint identity(1000000,1);

IF COL_LENGTH('PresetNoteGroup', 'PId') IS NOT NULL
  dbcc checkident(PresetNoteGroup,reseed,1000000)
ELSE  
  alter table PresetNoteGroup add PId bigint identity(1000000,1);

IF COL_LENGTH('PresetNotes', 'PId') IS NOT NULL
  dbcc checkident(PresetNotes,reseed,1000000)
ELSE  
  alter table PresetNotes add PId bigint identity(1000000,1);

IF COL_LENGTH('PrintCondition', 'PId') IS NOT NULL
  dbcc checkident(PrintCondition,reseed,1000000)
ELSE  
  alter table PrintCondition add PId bigint identity(1000000,1);

IF COL_LENGTH('PrinterDevice', 'PId') IS NOT NULL
  dbcc checkident(PrinterDevice,reseed,1000000)
ELSE  
  alter table PrinterDevice add PId bigint identity(1000000,1);

IF COL_LENGTH('PrinterDeviceItem', 'PId') IS NOT NULL
  dbcc checkident(PrinterDeviceItem,reseed,1000000)
ELSE  
  alter table PrinterDeviceItem add PId bigint identity(1000000,1);

IF COL_LENGTH('printertask', 'PId') IS NOT NULL
  dbcc checkident(printertask,reseed,1000000)
ELSE  
  alter table printertask add PId bigint identity(1000000,1);


IF COL_LENGTH('Profile', 'PId') IS NOT NULL
  dbcc checkident(Profile,reseed,1000000)
ELSE  
  alter table Profile add PId bigint identity(1000000,1);

IF COL_LENGTH('PurchaseHead', 'PId') IS NOT NULL
  dbcc checkident(PurchaseHead,reseed,1000000)
ELSE  
  alter table PurchaseHead add PId bigint identity(1000000,1);

IF COL_LENGTH('PurchaseItem', 'PId') IS NOT NULL
  dbcc checkident(PurchaseItem,reseed,1000000)
ELSE  
  alter table PurchaseItem add PId bigint identity(1000000,1);

IF COL_LENGTH('RecvAcct', 'PId') IS NOT NULL
  dbcc checkident(RecvAcct,reseed,1000000)
ELSE  
  alter table RecvAcct add PId bigint identity(1000000,1);

IF COL_LENGTH('SecondDisplayParams', 'PId') IS NOT NULL
  dbcc checkident(SecondDisplayParams,reseed,1000000)
ELSE  
  alter table SecondDisplayParams add PId bigint identity(1000000,1);

IF COL_LENGTH('SelfOrderingEvents', 'PId') IS NOT NULL
  dbcc checkident(SelfOrderingEvents,reseed,1000000)
ELSE  
  alter table SelfOrderingEvents add PId bigint identity(1000000,1);


IF COL_LENGTH('specialdaytable', 'PId') IS NOT NULL
  dbcc checkident(specialdaytable,reseed,1000000)
ELSE  
  alter table specialdaytable add PId bigint identity(1000000,1);

IF COL_LENGTH('StockH', 'PId') IS NOT NULL
  dbcc checkident(StockH,reseed,1000000)
ELSE  
  alter table StockH add PId bigint identity(1000000,1);

IF COL_LENGTH('StockI', 'PId') IS NOT NULL
  dbcc checkident(StockI,reseed,1000000)
ELSE  
  alter table StockI add PId bigint identity(1000000,1);

IF COL_LENGTH('StockLinkTable', 'PId') IS NOT NULL
  dbcc checkident(StockLinkTable,reseed,1000000)
ELSE  
  alter table StockLinkTable add PId bigint identity(1000000,1);

IF COL_LENGTH('StockTable', 'PId') IS NOT NULL
  dbcc checkident(StockTable,reseed,1000000)
ELSE  
  alter table StockTable add PId bigint identity(1000000,1);

IF COL_LENGTH('StockTakeHead', 'PId') IS NOT NULL
  dbcc checkident(StockTakeHead,reseed,1000000)
ELSE  
  alter table StockTakeHead add PId bigint identity(1000000,1);

IF COL_LENGTH('StockTakeItem', 'PId') IS NOT NULL
  dbcc checkident(StockTakeItem,reseed,1000000)
ELSE  
  alter table StockTakeItem add PId bigint identity(1000000,1);

IF COL_LENGTH('StreetTable', 'PId') IS NOT NULL
  dbcc checkident(StreetTable,reseed,1000000)
ELSE  
  alter table StreetTable add PId bigint identity(1000000,1);

IF COL_LENGTH('SubItemGroup', 'PId') IS NOT NULL
  dbcc checkident(SubItemGroup,reseed,1000000)
ELSE  
  alter table SubItemGroup add PId bigint identity(1000000,1);

IF COL_LENGTH('SubMenuLinkDetail', 'PId') IS NOT NULL
  dbcc checkident(SubMenuLinkDetail,reseed,1000000)
ELSE  
  alter table SubMenuLinkDetail add PId bigint identity(1000000,1);

IF COL_LENGTH('SubMenuLinkHead', 'PId') IS NOT NULL
  dbcc checkident(SubMenuLinkHead,reseed,1000000)
ELSE  
  alter table SubMenuLinkHead add PId bigint identity(1000000,1);

IF COL_LENGTH('Supplier', 'PId') IS NOT NULL
  dbcc checkident(Supplier,reseed,1000000)
ELSE  
  alter table Supplier add PId bigint identity(1000000,1);

IF COL_LENGTH('SupplierMemo', 'PId') IS NOT NULL
  dbcc checkident(SupplierMemo,reseed,1000000)
ELSE  
  alter table SupplierMemo add PId bigint identity(1000000,1);

IF COL_LENGTH('SysLog', 'PId') IS NOT NULL
  dbcc checkident(SysLog,reseed,1000000)
ELSE  
  alter table SysLog add PId bigint identity(1000000,1);

IF COL_LENGTH('sysparameter', 'PId') IS NOT NULL
  dbcc checkident(sysparameter,reseed,1000000)
ELSE  
  alter table sysparameter add PId bigint identity(1000000,1);

IF COL_LENGTH('TablePage', 'PId') IS NOT NULL
  dbcc checkident(TablePage,reseed,1000000)
ELSE  
  alter table TablePage add PId bigint identity(1000000,1);

IF COL_LENGTH('TableSet', 'PId') IS NOT NULL
  dbcc checkident(TableSet,reseed,1000000)
ELSE  
  alter table TableSet add PId bigint identity(1000000,1);

IF COL_LENGTH('TrackingSource', 'PId') IS NOT NULL
  dbcc checkident(TrackingSource,reseed,1000000)
ELSE  
  alter table TrackingSource add PId bigint identity(1000000,1);

IF COL_LENGTH('TrackingSync', 'PId') IS NOT NULL
  dbcc checkident(TrackingSync,reseed,1000000)
ELSE  
  alter table TrackingSync add PId bigint identity(1000000,1);

IF COL_LENGTH('TyroReconciliation', 'PId') IS NOT NULL
  dbcc checkident(TyroReconciliation,reseed,1000000)
ELSE  
  alter table TyroReconciliation add PId bigint identity(1000000,1);

IF COL_LENGTH('TyroReconcilTransaction', 'PId') IS NOT NULL
  dbcc checkident(TyroReconcilTransaction,reseed,1000000)
ELSE  
  alter table TyroReconcilTransaction add PId bigint identity(1000000,1);

IF COL_LENGTH('TyroReport', 'PId') IS NOT NULL
  dbcc checkident(TyroReport,reseed,1000000)
ELSE  
  alter table TyroReport add PId bigint identity(1000000,1);

IF COL_LENGTH('UserGroupTable', 'PId') IS NOT NULL
  dbcc checkident(UserGroupTable,reseed,1000000)
ELSE  
  alter table UserGroupTable add PId bigint identity(1000000,1);

IF COL_LENGTH('Version', 'PId') IS NOT NULL
  dbcc checkident(Version,reseed,1000000)
ELSE  
  alter table Version add PId bigint identity(1000000,1);

IF COL_LENGTH('VIPTable', 'PId') IS NOT NULL
  dbcc checkident(VIPTable,reseed,1000000)
ELSE  
  alter table VIPTable add PId bigint identity(1000000,1);

IF COL_LENGTH('VoidReasonTable', 'PId') IS NOT NULL
  dbcc checkident(VoidReasonTable,reseed,1000000)
ELSE  
  alter table VoidReasonTable add PId bigint identity(1000000,1);

IF COL_LENGTH('WastageHead', 'PId') IS NOT NULL
  dbcc checkident(WastageHead,reseed,1000000)
ELSE  
  alter table WastageHead add PId bigint identity(1000000,1);

IF COL_LENGTH('WastageItem', 'PId') IS NOT NULL
  dbcc checkident(WastageItem,reseed,1000000)
ELSE  
  alter table WastageItem add PId bigint identity(1000000,1);
  
   ''')
   
    
def completeSingleSQLFile():
    fileName = SingleSqlFile
    if os.path.exists(fileName):
        f = open(fileName, "a", encoding='utf-8')
        f.write('\n EXEC sp_MSforeachtable @command1="ALTER TABLE ? ENABLE TRIGGER ALL;" \n')
        
def writeToSingleSQLFile(tableName,cols,f_values):
    fileName = SingleSqlFile
    if os.path.exists(fileName):
        f = open(fileName, "a", encoding='utf-8')
        f.write("\ntruncate table "+tableName+" ; ")
    if  tableName!="SequenceID" and tableName!="DiscountSchema":
        f.write("\nSET IDENTITY_INSERT "+ tableName+" ON; \n")
    sql = f"insert into {tableName} ({cols}) values {f_values}; " 
    f.write(sql)
    if  tableName!="SequenceID" and tableName!="DiscountSchema":  
        f.write("\nSET IDENTITY_INSERT "+ tableName+" OFF;\n")
    f.close()


    
def writeToSingleSQLFileType2(tableName,cols,values):
    fileName = SingleSqlFile
    if os.path.exists(fileName):
        f = open(fileName, "a", encoding='utf-8')
        f.write("\ntruncate table "+tableName+" ; ")
        
    # if  tableName!="SequenceID" and tableName!="DiscountSchema":
    #     f.write("\nSET IDENTITY_INSERT "+ tableName+" ON; \n")
        
    # f = open(fileName, "a", encoding='utf-8')
    # f.write("\ntruncate table "+tableName+" ; ")
    
    if tableName!="SequenceID" and tableName!="DiscountSchema" :
        f.write("\nSET IDENTITY_INSERT "+ tableName+" ON;")
      
    
    dataIndex =0
    while dataIndex < len(values):
          values[dataIndex] = re.sub(r"('None')", "NULL", values[dataIndex])
          values[dataIndex] = re.sub(r"('nan')", "0", values[dataIndex])
          values[dataIndex] = re.sub(r"('0.0')", "0", values[dataIndex])
          sql = f"\ninsert into {tableName} ({cols}) values ({values[dataIndex]}); " 
          f.write(sql)
          dataIndex=dataIndex+1
        
    if  tableName!="SequenceID" and tableName!="DiscountSchema":  
        f.write("\nSET IDENTITY_INSERT "+ tableName+" OFF;\n")
    f.close()
               

def closesystem():
    sys.exit()
    


def writeToSQLFile(tableName,Data):
    
    cols = ', '.join(Data.columns.to_list()) 
    vals = []
    for index, r in Data.iterrows():
        row = []
        for x in r:
            row.append(f"'{str(x)}'")

        row_str = ', '.join(row)
        vals.append(row_str)
    f_values = [] 
    for v in vals:
        f_values.append(f'\n ({v})')
    # Handle inputting NULL values
    f_values = ', '.join(f_values) 
    f_values = re.sub(r"('None')", "NULL", f_values)
    f_values = re.sub(r"('nan')", "0", f_values)
    f_values = re.sub(r"('0.0')", "0", f_values)
    
    
  
    #print(sql)   
    fileName=directory+'\\'+tableName +'.sql'
    if os.path.exists(fileName):
        os.remove(fileName)
        
        
    print("SQL " + tableName)
    f = open(fileName, "a", encoding='utf-8')
    f.write("\ntruncate table "+tableName+" ; ")
    
    if tableName!="SequenceID" and tableName!="DiscountSchema" :
        f.write("\nSET IDENTITY_INSERT "+ tableName+" ON;")
        
    sql = f"insert into {tableName} ({cols}) values {f_values}; " 
    f.write(sql)
    
    if  tableName!="SequenceID" and tableName!="DiscountSchema":  
        f.write("\nSET IDENTITY_INSERT "+ tableName+" OFF;\n")
    f.close()
    
    if tableName!="OrderH" and tableName!="OrderI" and tableName!="RecvAcct":
      writeToSingleSQLFile(tableName,cols,f_values)



def writeToSQLFileLineByLine(tableName,Data):
      
    Data = Data.replace("'","''", regex=True)

    
    cols = ', '.join(Data.columns.to_list()) 
    vals = []
    for index, r in Data.iterrows():
        row = []
        for x in r:
            row.append(f"'{str(x)}'")

        row_str = ', '.join(row)
        vals.append(row_str)
     
    fileName=directory+'\\'+tableName +'.sql'
    if os.path.exists(fileName):
        os.remove(fileName)
        
        
    print("SQL " + tableName)
    f = open(fileName, "a", encoding='utf-8')
    f.write("\ntruncate table "+tableName+" ; ")
    
    if tableName!="SequenceID" and tableName!="DiscountSchema" :
        f.write("\nSET IDENTITY_INSERT "+ tableName+" ON;")
        
    dataIndex =0
    
    while dataIndex < len(vals):
          vals[dataIndex] = re.sub(r"('None')", "NULL", vals[dataIndex])
          vals[dataIndex] = re.sub(r"('nan')", "0", vals[dataIndex])
          vals[dataIndex] = re.sub(r"('0.0')", "0", vals[dataIndex])
          
          sql = f"\ninsert into {tableName} ({cols}) values ({vals[dataIndex]}); " 
          f.write(sql)
          dataIndex=dataIndex+1
          
    if  tableName!="SequenceID" and tableName!="DiscountSchema":  
        f.write("\nSET IDENTITY_INSERT "+ tableName+" OFF;\n")
    f.close()
          
    if tableName!="OrderH" and tableName!="OrderI" and tableName!="RecvAcct":
          writeToSingleSQLFileType2(tableName,cols,vals)
          #writeToSingleSQLFile(tableName,cols,vals)
    
    
  




def writeToExcelFile(tableName,Data):
    
    print("Excel " +tableName )
    Export_file=directory+"\\" + tableName +".xlsx"
    Data.to_excel(Export_file, index = False, header=True,engine='xlsxwriter')
        



def processAssessMenuTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT  AuthoriseCloseWindow,AuthoriseDiscount,BookingFormConditionSetupMenu,DailyReportMenu,DatabaseBackupMenu,DatabaseRestoreMenu,InvoiceConditionSetupMenu,OpenCashDrawerMenu,PaymentAuthority,PrintInvoiceAuthority,PrintJobListAuthority,TableInformationSetupMenu,StaffName,SecureCode,Supervisor,BookingListMenu,StockReceiveMenu,InquirySalesHistoryMenu,VIPInformationMenu,SalesReportMenu,SalesStatisticsReportMenu,StockReportMenu,StockReceiveReportMenu,StatisticsChartMenu,SupplierInformationListMenu,ExpensesDescriptionSetupMenu,ExpensesDataEntryMenu,ExpensesReportMenu,ReceiptsReportMenu,PaymentsReportMenu,GSTPayableReportMenu,ProfileSetupMenu,PrinterSetupMenu,CategorySetupMenu,MenuSetupMenu,PaymentsMethodSetupMenu,SupplierInformationSetupMenu,Birthday,Telephone,Mobile,Fax,Address,Rate,AttendanceReportMenu,VoidItemAuthority,PurchaseOrderMenu,PurchasePayableMenu,TableOrderMenu,PointOfSalesMenu,CheckDailyReport,AuthoriseRefund,UserManager,AllowEditOrder,PrintDailyReport,DrawerPortNumber,DefaultDrawerPortNumber,EditAttendanceRecord,StockAdjustmentMenu,StockAdjustmentReportMenu,PhoneOrderMenu,CashPayOutMenu,CashFloatMenu,AssignDriverAuthorised,DepositMenu,WastageMenu,WastageReportMenu,AuthrisedCancelHoldOrder,ManuallyEnterDiscountRate,EditOrderPayment,InquirySalesRelatedReportDays,CashDeclarationReportMenu,AccountEnabled,AuthorizedChangeQty,AuthorizedChangePrice,DeleteVIPRecord,ControlButtonSetup,DiscountRateSetup,VoidItemDescriptionSetup,EFTPOSUtility,ChangeMenuStatus,StockTakeMenu,StockTakeReportMenu,UserGroupSetupAuthorized,UploadMembersRewardsMenu,PId,SettingsPortalMenu,ZiiTOTableLockMenu,StaffCode,FirstName,LastName,ZiiOnlineOrderCancel,OverrideSalesPrice, STRFTIME('%Y-%m-%d %H:%M:%S', LastUpdatedTime) as LastUpdatedTime  FROM AccessMenu;"
    
   
    AccessMenu = pd.read_sql_query(Query, Connection)

   
    Connection.close()
    
    
    QuerySize = len(AccessMenu)
    if QuerySize>0:
        writeToSQLFileLineByLine("AccessMenu",AccessMenu)
        writeToExcelFile("AccessMenu",AccessMenu)
    
    


def processDiscountRateTableTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Description, DiscountRate,DiscountKind,PId FROM DiscountRateTable;" 
    DiscountRateTable = pd.read_sql_query(Query, Connection)
        
    Connection.close()
    
    QuerySize = len(DiscountRateTable)
    if QuerySize>0:
        DiscountRateTable["DiscountRate"]=pd.to_numeric(DiscountRateTable["DiscountRate"])
        writeToSQLFileLineByLine("DiscountRateTable",DiscountRateTable)
        writeToExcelFile("DiscountRateTable",DiscountRateTable)
    
    
      


def processDiscountSchemaTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT SchemaCode, SchemaName,Rate,Kind,Active,CreateBy,STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt FROM DiscountSchema;" 
    DiscountSchema = pd.read_sql_query(Query, Connection)
             
    
    Connection.close()
    
    
    QuerySize = len(DiscountSchema)
    if QuerySize>0:
        writeToSQLFileLineByLine("DiscountSchema",DiscountSchema)
        writeToExcelFile("DiscountSchema",DiscountSchema)  
    
   
    
    
    
    

def processChargeScopeTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT ChargeRate,Model,Frequency,StartTime,EndTime,ApplyOnDineIn,ApplyOnTakeaway,ApplyOnQuickSale,ApplyOnDelivery,ApplyOnPickup,STRFTIME('%Y-%m-%d %H:%M:%S', CreatedAt) as  CreatedAt, STRFTIME('%Y-%m-%d %H:%M:%S', UpdatedAt) as UpdatedAt ,PId FROM ChargeScope" 
    ChargeScope = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(ChargeScope)
    if QuerySize>0:
        ChargeScope["ChargeRate"]=pd.to_numeric(ChargeScope["ChargeRate"])
        writeToSQLFileLineByLine("ChargeScope",ChargeScope)
        writeToExcelFile("ChargeScope",ChargeScope)      
      
        


   

def processDrawerDeviceTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,DrawerNo,ConnectToNo,Speed,PinModel,CheckStatus,DrawerMode,Enabled,Description FROM DrawerDevice" 
    
    DrawerDevice = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(DrawerDevice)
    if QuerySize>0:
        writeToSQLFileLineByLine("DrawerDevice",DrawerDevice)
        writeToExcelFile("DrawerDevice",DrawerDevice)  


def processMachineIDTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    
    Query = "SELECT MachineID,PId,DefaultCheckListPrinter,DefaultDrawerNo,Description,DefaultPrinter,ClientUniqueId,Disabled,STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt , STRFTIME('%Y-%m-%d %H:%M:%S', BindAt) as BindAt ,EnableEftposProduce,DefaultKitchenScreen,MachineType,IpAddress,FixedJobListPrinter FROM MachineID" 
    
    MachineID = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(MachineID)
    if QuerySize>0:
        writeToSQLFileLineByLine("MachineID",MachineID)
        writeToExcelFile("MachineID",MachineID)  
        

def processPaymentTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT ShowOnList,Payment,SurchargeRate,Code,EFTPOSPayment,LinkToDevice,PId,CounterPayment,SupportCasher,SupportSelfPad,OrderIndex,SupportOrderingTerminal,SpecialChargeRate,XeroAccountCode,XeroAccountId FROM Payment" 
    
    Payment = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(Payment)
    if QuerySize>0:
        Payment["SurchargeRate"] = pd.to_numeric(Payment["SurchargeRate"] )
        Payment["SpecialChargeRate"] = pd.to_numeric(Payment["SpecialChargeRate"])
        writeToSQLFileLineByLine("Payment",Payment)
        writeToExcelFile("Payment",Payment)  


def processPrintConditionTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,BillCondition,InvoiceCondition,BookingFormCondition,BuzId FROM PrintCondition" 
    
    PrintCondition = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(PrintCondition)
    if QuerySize>0:
        writeToSQLFileLineByLine("PrintCondition",PrintCondition)
        writeToExcelFile("PrintCondition",PrintCondition)  
        

def processPrinterDeviceTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,DefaultPrinterIDNo,MobileDefaultPrinterIDNo,CheckListPrinterIDNo,SupportChinese,PrintLogoOnPOSPrinter,FeedLinesBeforeCut,FeedLinesBeforePringJob,DefaultDrawerNo,IntegratedEFTReceipt,BuzId FROM PrinterDevice" 
    
    PrinterDevice = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(PrinterDevice)
    if QuerySize>0:
       
        writeToSQLFileLineByLine("PrinterDevice",PrinterDevice)
        writeToExcelFile("PrinterDevice",PrinterDevice)  
        
        
        
        
        
        
        
        
def processPrinterDeviceItemTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "  SELECT PId,PrinterNo,ModelType,PortType,PortSetting,PrinterName,TableOrderJobListTitle,QuickServiceJobListTitle,PhoneOrderJobListTitle,JobListDuplicate,GoWithMessage,SupportGraphic,Thermal,JobListCopies FROM PrinterDeviceItem" 
    
    PrinterDeviceItem = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(PrinterDeviceItem)
    if QuerySize>0:
  
        writeToSQLFileLineByLine("PrinterDeviceItem",PrinterDeviceItem)
        writeToExcelFile("PrinterDeviceItem",PrinterDeviceItem)  
        
                
def processProfileTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = " SELECT BeginTime,CheckPassword,EndTime,MainCategoryLine,MainMenuLine,NotAllowModify,POSCategoryLine,POSMenuLine,CompanyName,Telephone,Fax,ABN,Address,Initial,ButtonLayOut,ServiceChargeRate,TableTracking,PersonCount,CheckTableStatus,PrintBillNo,RoundingFlag,ForceVIPDiscount,AutoOpenTill,AutoPrintJobList,PrintServiceOnJobList,PrintPersonsOnJobList,PrintPriceOnJobList,PrintTimeOnInvoice,HappyHour,HappyHourStartTime,HappyHourEndTime,ShowTaxOnSalesSection,POSJobList,POSOrderList,POSInvoice,PrintPickupSlip,PrintCategoryColor,OrderListDescription,InvoiceDescription,PrintBillCategory,PrintInvoiceCategory,VIPDefaultSearch,AutoPrintPhoneOrderJobList,AutoInstructionSelection,PrintTableNo,PrintDateOnDailyReport,AutoPrintBill,AutoPrintInvoice,AutoPriceWindow,PrintZeroPriceItemOnInvoice,AutoPopVoidReason,ManuallyEnterTableNumber,PrintInvoiceNo,AutoSaveOrder,ScaleBarcode,PrintGoWithInstruction,PrintOpNameOnJobList,AutoPrintMergedOrder,AutoPrintJobListForHoldOrder,AutoSurcharge,SurchargeStartTime,SurchargeEndTime,HappyHourStartTime1,HappyHourEndTime1,HappyHourStartTime2,HappyHourEndTime2,HappyHourStartTime3,HappyHourEndTime3,HappyHourStartTime4,HappyHourEndTime4,HappyHourStartTime5,HappyHourEndTime5,HappyHourStartTime6,HappyHourEndTime6,SurchargeName,OtherCharge,OtherChargeName,OtherChargeRate,PriceIncludesGST,DefaultGSTRate,DefaultVIPState,PrintIngredientsOnJobList,MaxDiscountPercentage,MaxDollarDiscount,JobListFontSize,DefaultBackupPath,ShowPrintInvoiceWindow,ChangeQtyWithCondiment,CompulsoryEnterCustomerName,AutoPrintCheckList,PrintOrderNoOnJobList,AutoBackup,BackupTime,PhoneOrderMenuLine,PhoneOrderCategoryLine,ManuallyPrintJobList,PhoneOrderJobListFormat,BackupFrequency,BackupOnceTime,DiscountRateEnterMode,ShowNegativeQty,PrintOrderNoOnTaxInvoice,CheckListFormat,AutoLogout,AutoLogoutTimeOut,PrintRedColorQtyOnJobList,MinimumChargeKind,OnlyOpenDrawerForCashPayment,MinimumChargeItemCode,MinimumChargePerPerson,PrintDiscountRateOnBill,OnlyPrintSimpleFormatDailyReport,OnlyPrintLastTwoDigitalOrderNo,CheckPrinterStatus,AutoPrintBillWhenPhoneOrderSaved,AutoAddDeliveryChargeForPhoneOrder,DeliveryChargeItemCode,PrintZeroQtyItemsOnJobList,JobListFormatForPrinter1,JobListFormatForPrinter2,JobListFormatForPrinter3,JobListFormatForPrinter4,JobListFormatForPrinter5,JobListFormatForPrinter6,JobListFormatForPrinter7,JobListFormatForPrinter8,JobListFormatForPrinter9,JobListFormatForPrinter10,JobListFormatForPrinter11,JobListFormatForPrinter12,SecondDisplayDescription,ForceCashDeclaration,SubMenuStyle,RemindVIPBirthday,PrintOrderDateOnJobList,AutoWeightScalableItem,CheckListDescription,JobListRelateFormat,TableServiceJobListFormat,QuickServiceJobListFormat,PrintCustomerNameOnJobList,DoNotPrintVoidItemsOnJobList,PrintTableNumberChoice,EnableWeekendPriceFunction,WeekendPriceStartDay,WeekendPriceEndDay,SelfOrderConsole,KeepCancelSales,PrintSpellInstructionOnBill,PrintServicePeopleNameOnInvoice,PrintTotalOnCheckList,PrintCustomerDetailOnInvoice,DefaultPhoneOrderKind,CustomerNameEnterKeypad,PrintItemInRedForJobList,InstructionItemsPrintToOwnPrinters,PrintVoidItemOnDailyReport,PrintGroupSalesOnDailyReport,PrintNonSalesOpenDrawerOnDailyReport,EnableEatInTakeAwayFunction,AutoSetPhoneOrderDueTime,DefaultPhoneOrderDueTime,AutoIssueVoucher,VoucherSalesAmount,VoucherDescription,PromotionDiscountTerm,SubMenuSortBy,LoyaltyReward,RewardPointsRate,RedeemPointsRate,ConnectionKind,URL,RewardsKind,EnablePagerFunction,ElapseTimeKind,DoNotPrintVoidItemOnInvoice,KeypadButtonLinks,OnlyPrintNewItemOnCheckList,PrintReprintSymbolOnJobList,PrintOrderNumberOnInvoiceTop,PrintOrderNumberOnBillTop,DefaultServiceKind,ForceSelectPaymentMethod,BookingTableStatusKind,PrintAmountOnPickupSlip,EnterCustomerIDForHoldOrder,PrintConsolidatedItemsOnJobList,PrintTableMergeInformation,PrintSeatNumberOnJobList,PrintGratuityFillInSpaceOnBill,PrintSmallFontForInstructionItemOnJobList,PrintJobListAfterEachPayment,AutoPrintAttendanceSlip,DefaultStockItemSearch,ForceToOpenLockedTable,ForceOpenLockedTableWithComfirmInfo,JobListDescriptionforPrinter1,JobListDescriptionforPrinter2,JobListDescriptionforPrinter3,JobListDescriptionforPrinter4,JobListDescriptionforPrinter5,JobListDescriptionforPrinter6,JobListDescriptionforPrinter7,JobListDescriptionforPrinter8,JobListDescriptionforPrinter9,JobListDescriptionforPrinter10,JobListDescriptionforPrinter11,JobListDescriptionforPrinter12,JobListSecondDescription1,JobListSecondDescription2,JobListSecondDescription3,JobListSecondDescription4,JobListSecondDescription5,JobListSecondDescription6,JobListSecondDescription7,JobListSecondDescription8,JobListSecondDescription9,JobListSecondDescription10,JobListSecondDescription11,JobListSecondDescription12,UseOriginalItemPrice,SaturdayWageRate,SundayWageRate,PublicHolidayWageRate,ShowSeatNumberAsSpellInstruction,ForceSelectTakeAwayOrEatIn,DefaultCreditCardSurchargeRate,PrintPaymentDetail,JobListTimeFormat,ShowMemberIDOnOrderScreen,OnlyShowMemberFirstName,CheckVoucherIDViaInternet,GiftcardExpireDays,AutoPrintParkingVoucher,ResetMenuButtonForNewOrder,ChioceMenuGroupForiMenu,NotConsolidateForEachItemOnDifferentDockect,EnablePresetNotes,NotesAtJobListPosition,ShowNotesOnOrderForm,CalculateOtherChargeKind,SmallButtonForQuickSales,PaymentChangeForwardToTips,PrintCreditCardPaymentOption,EFTPOSPaymentSurchargeApplyToTips,ShowElapseTime,PId,DineInPriorityCheckout,SupportMultiLanguage,EnableDineIn,EnableTakeAway,EnableQuickService,LinkEFTPOSType,AutoSendJobListToScreen,KitchenScreenReminderTime,BuzId,EnableQuickCheckOut,EnableSpecialDay,BookingAccessKind,EnableDelivery,EnablePickUp,OrderTypeFirstChoice,PrintCourseItemVerbally,PrintCourseAndSendIfNeed,PrintCourseWhenCalled,PrintConsolidatedItemsOnInvoiceBill,TableTimeLimit,PrintMembershipQrcodeOnBill,PrintMembershipDescriptionOnBill,OrderItemNoteEnabled,OrderNoteEnabled,PrintPickNoOnCheckList,PrintOnlineNoOnJobList,PrintOrderNoOnLableJobList,PrintOnlineNoOnInvoiceBill,PrintConsolidatedInstructionsOnJobList,PrintConsolidatedInstructionsOnInvoiceBill,NotConsolidateForEachInsOnDifferentDockect,AutoPrintTakeAwayJobList,AutoPrintTakeAwayBill,AutoPrintTakeAwayInvoice,AutoPrintPickUpJobList,AutoPrintPickUpBill,AutoPrintPickUpInvoice,AutoPrintDeliveryJobList,AutoPrintDeliveryBill,AutoPrintDeliveryInvoice,PrintCopiesQtyOnJobList,QRCodePayType,PrintCustNameInsteadOnLabelJobList,SplitPrintMultiOrdered FROM Profile" 
    
    Profile = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(Profile)
    if QuerySize>0:
        
        writeToSQLFileLineByLine("Profile",Profile)
        writeToExcelFile("Profile",Profile)  
        
        
              
def processEftMachinePairTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId ,MachineID ,TerminalID ,IntegrationKey , STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt ,IntegratedReceipt ,IntegratedSurcharge ,EFTPOSType ,EftEnvironment ,SerialNumber ,SecretsEncKey ,SecretsHmacKey ,EftPosAddress ,LinklyPosId ,LinklyPosVendorId ,Username ,Password ,MerID ,EftPort ,StationId ,TenantCode ,TenantName FROM EftMachinePair" 
    
    EftMachinePair = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(EftMachinePair)
    if QuerySize>0:
        writeToSQLFileLineByLine("EftMachinePair",EftMachinePair)
        writeToExcelFile("EftMachinePair",EftMachinePair)  




        
def processSequenceIDTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT SequenceId,ItemCode,NowNumber   FROM SequenceID" 
    
    SequenceID = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SequenceID)
    if QuerySize>0:
        
        writeToSQLFileLineByLine("SequenceID",SequenceID)
        writeToExcelFile("SequenceID",SequenceID)  
        


def processTablePageTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PageNo,Description,PId   FROM TablePage " 
    
    TablePage = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(TablePage)
    if QuerySize>0:
        
        writeToSQLFileLineByLine("TablePage",TablePage)
        writeToExcelFile("TablePage",TablePage)  
        
        
        

def processTableSetTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Status,TableNo,Seats,FontName,FontSize,FontBold,FontItalic,FontUnderline,FontStrikeout,ButtonShape,ButtonWidth,ButtonHeight,ButtonX,ButtonY,PropertyFlag,Description,PageFlag,PDAPosition,MinimumChargePerTable,ServiceStatus,IPAddress,SelfOrderStatus,TerminalConnected,TableLockerName,OnlineOrderTable,PId,ZiiTOTableLockName,TeamNo, STRFTIME('%Y-%m-%d %H:%M:%S', LockUpdateTime) as LockUpdateTime , STRFTIME('%Y-%m-%d %H:%M:%S', TeamLocalTime) as TeamLocalTime  FROM TableSet" 
    
    #STRFTIME('%Y-%m-%d %H:%M:%S', BindAt) as BindAt
    
    TableSet = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(TableSet)
    if QuerySize>0:
        
        writeToSQLFileLineByLine("TableSet",TableSet)
        writeToExcelFile("TableSet",TableSet)  
        

def processSysparameterTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT ParamCode,ParamValue,ParamValueEx,ParamType,Notes,OrderIndex,PId FROM sysparameter" 
    
    sysparameter = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(sysparameter)
    if QuerySize>0:
        
        writeToSQLFileLineByLine("sysparameter",sysparameter)
        writeToExcelFile("sysparameter",sysparameter)  
        
   
def processspecialdaytableTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT SpecialStartDate,SpecialEndDate,Active,Description1,Description2,PId FROM specialdaytable" 
    
    specialdaytable = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(specialdaytable)
    if QuerySize>0:
        writeToSQLFileLineByLine("specialdaytable",specialdaytable)
        writeToExcelFile("specialdaytable",specialdaytable)  
        
        
#--------------------Business DATA-----------------------------------        


def processRecvAcctTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Transfer,OrderNo, STRFTIME('%Y-%m-%d %H:%M:%S', AccountDate) as AccountDate ,PaidAmount,Payby,IDNo,OpName,MachineID,DepositID,GiftCardBalance, STRFTIME('%Y-%m-%d %H:%M:%S', GiftCardExpireDate) as GiftCardExpireDate ,Notes,PId,Surcharge,Tips,PaymentFlag,RelatedRecvID,PaymentActivityBuzId,SpecialCharge FROM RecvAcct" 
    
    RecvAcct = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(RecvAcct)
    if QuerySize>0:
       
        writeToSQLFileLineByLine("RecvAcct",RecvAcct)
        writeToExcelFile("Z_RecvAcct",RecvAcct)  
        

def processOrderHTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT BookingNo,Credit,OrderPrinted,Tips,STRFTIME('%Y-%m-%d %H:%M:%S', OrderDate) as OrderDate  ,OrderNo,Persons,TableNo,ServicePerson,Amount,GST,PaidAmount,InvoiceNo,VIPNo,OpName,ServiceCharge,ServiceChargeRate,Surcharge,MachineID,BillKind,DollarDiscount, STRFTIME('%Y-%m-%d %H:%M:%S', DueTime) as DueTime,DiscountKind,Delivery,OtherCharge,OtherChargeRate,PriceIncludesGST,CurrentGSTRate,SplitBill,CustomerName,DiscountOperator,MemberID,CurrentPoints,CustomerAddress,CustomerTelephone,PointsUploaded,AwardEffective,PresetDiscountCode,VoucherID,VoucherAmount,VoucherDiscount,RedeemPoints,TotalRedeemPoints,SelfOrderMenuGroup,Notes,PId,SourceType,SourceKind,PackageCharge, STRFTIME('%Y-%m-%d %H:%M:%S', CheckoutCompleteTime) as CheckoutCompleteTime ,DeliveryFee,PayAfterDinner,OnlineOrderId, STRFTIME('%Y-%m-%d %H:%M:%S', BuzUpdateAt) as BuzUpdateAt ,STRFTIME('%Y-%m-%d %H:%M:%S', EndDueTime) as EndDueTime , STRFTIME('%Y-%m-%d %H:%M:%S', HoldTime) as HoldTime ,SourceOrderType,TeamNo,TeamTables,PayMode,ChannelOrderDisplayId,Channel,SpecialCharge,Kids,ManualServiceChargeRate,ExperienceFlag,PendingOrder,NotifyStatus, STRFTIME('%Y-%m-%d %H:%M:%S', NotifyAt) as NotifyAt ,CrmSeq,GuestId,DropFraction   FROM OrderH" 
    
    OrderH = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(OrderH)
    if QuerySize>0:
       
        writeToSQLFileLineByLine("OrderH",OrderH)
        writeToExcelFile("Z_OrderH",OrderH)  
        

def processOrderITable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Condition,PaidQty,PriceSelect,Seat,OrderNo,ItemCode,Qty,Price,Discount,TaxRate,IDNo,PrintFlag,SentToKitchen,VoidReason,SpecialOrder,CheckListPrinted,VoidFlag,OrderOperator,OriginalPrice,PresetDiscountCode,OriginalQty,RedeemItem,ManuallyEnterWeight,PId,RedeemPoints,PackagePrice,SeatNumber,CourseCode,CourseSendFlag,OtherChargeItem,OrderIndex,OnlineItemId,STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt ,BatchNumber,ParentItemCode,ParentSerialNo,SerialNo,SourceSerialNo, STRFTIME('%Y-%m-%d %H:%M:%S', BuzUpdateAt) as BuzUpdateAt  ,CoursePrintFlag,ServiceName,ServiceCode,CategoryCode,GiftFlag,AllowGift,Scalable,TareWeight,SourceIdNo,WasteInfo,OrderFrequency,ItemFrequency,STRFTIME('%Y-%m-%d %H:%M:%S', PendingEndAt) as PendingEndAt ,PendingFlag,LastBatchNumber  FROM OrderI" 
    
    OrderI = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(OrderI)
    if QuerySize>0:
       
        writeToSQLFileLineByLine("OrderI",OrderI)
        writeToExcelFile("Z_OrderI",OrderI)  
        
        
        

        
                
# PrintCondition
# PrinterDevice
# PrinterDeviceItem
# Profile
# SequenceID
# TablePage
# TableSet



# OrderH

# OrderI
# PayAcct






def processTable_Category(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT ButtonColor , Code , FontColor , ShowOnMainMenu , ShowOnPOSMenu , Category , FontName , FontSize , FontBold , FontItalic , FontUnderline , FontStrikeout , Category1 , MenuGroupCode , ButtonColor1 , FontName1 , FontColor1 , FontSize1 , FontBold1 , FontItalic1 , FontUnderline1 , FontStrikeout1 , ShowOnPhoneOrderMenu , Category2 , Category3 , Enable , Notes , ShowOnSelfOrderMenu , OnlineOrderCategory , PId , OrderIndex , CourseCode , ShowOnDineInMenu , ShowOnTakeawayMenu , ShowOnQuickSaleMenu , ShowOnDeliveryMenu , ShowOnPickupMenu , MinimumChoiceQty , MaximumChoiceQty , OnlineStatus , QRCodeStatus , BorderColor , OnlineDisplayName1 , OnlineDisplayName2 , Version , MenuVersion FROM Category" 
    TableName = "Category"
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        writeToExcelFile(TableName,SQLData) 
        writeToSQLFileLineByLine(TableName,SQLData)
        
        







def processTable_CategoryMenuItem(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Category , ItemCode , STRFTIME('%Y-%m-%d %H:%M:%S', CreatedAt) as CreatedAt , STRFTIME('%Y-%m-%d %H:%M:%S', UpdatedAt) as UpdatedAt , PId , OrderIndex , Version , MenuVersion FROM CategoryMenuItem" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        #writeToSQLFileLineByLine("CategoryMenuItem",SQLData)
        writeToSQLFileLineByLine("CategoryMenuItem",SQLData)
        writeToExcelFile("CategoryMenuItem",SQLData) 
        









def processTable_course(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "course"
    Query = "SELECT CourseCode , Description1 , Description2 , OrderIndex , PId , Version , MenuVersion FROM course" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 








def processTable_InstructionLink(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "InstructionLink"
    Query = "SELECT Code , ItemCode , Kind , Qty , Price , Condition , ID , MaximunCharge , PId , MultiPrice , IsDefault , Version , MenuVersion FROM InstructionLink" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        writeToExcelFile(TableName,SQLData) 
        writeToSQLFileLineByLine(TableName,SQLData)
        










def processTable_InstructionLinkGroup(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "InstructionLinkGroup"
    Query = "SELECT PId , ItemCode , Kind , SubGroupCode , SingleChoice , MinNumberOfChoice , MaxNumberOfChoice , Version , MenuVersion FROM InstructionLinkGroup" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        writeToExcelFile(TableName,SQLData) 
        writeToSQLFileLineByLine(TableName,SQLData)
        









def processTable_ItemGroupTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "ItemGroupTable"
    Query = "SELECT GroupName , PId , Version , MenuVersion FROM ItemGroupTable" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        writeToExcelFile(TableName,SQLData) 
        writeToSQLFileLineByLine(TableName,SQLData)
        









def processTable_MenuGroupLinkCategory(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "MenuGroupLinkCategory"
    Query = "SELECT MenuGroupCode , CategoryCode , STRFTIME('%Y-%m-%d %H:%M:%S', CreatedAt) as CreatedAt , STRFTIME('%Y-%m-%d %H:%M:%S', UpdatedAt) as UpdatedAt , PId , OrderIndex , Version , MenuVersion FROM MenuGroupLinkCategory" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
        writeToExcelFile(TableName,SQLData) 
        writeToSQLFileLineByLine(TableName,SQLData)
        









def processTable_MenuGroupTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "MenuGroupTable"
    Query = "SELECT Code , Description , PId , ApplyToZiiTO , ApplyToKiosk , ApplyToOnline , ApplyToQRCode , Version , MenuVersion FROM MenuGroupTable " 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
   
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        












def processTable_MenuGroupTimes(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "MenuGroupTimes"
    Query = "SELECT BuzId , TimeName , StartTime , EndTime , MenuGroupCode , STRFTIME('%Y-%m-%d %H:%M:%S', CreatedAt) as CreatedAt , STRFTIME('%Y-%m-%d %H:%M:%S', UpdatedAt) as UpdatedAt , PId , Version , MenuVersion FROM MenuGroupTimes" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        





def processTable_MenuItem(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "MenuItem"
    Query = "SELECT BarCode , BarCode1 , BarCode2 , BarCode3 , ButtonColor , FontColor , Instruction , Multiple , Price1 , Price2 , Price3 , SubDescription , SubDescription1 , SubDescription2 , SubDescription3 , ItemCode , Description1 , Description2 , Price , TaxRate , Category , Active , PrinterPort , FontName , FontSize , FontBold , FontItalic , FontUnderline , FontStrikeout , AllowDiscount , JobListColor , OpenPrice , PrinterPort1 , PrinterPort2 , HappyHourPrice1 , HappyHourPrice2 , HappyHourPrice3 , HappyHourPrice4 , DefaultQty , SubDescriptionSwap , MainPosition , POSPosition , KitchenScreenFontColor , PrinterPort3 , ItemGroup , OnlyShowOnSubMenu , ButtonColor1 , FontName1 , FontColor1 , FontSize1 , FontBold1 , FontItalic1 , FontUnderline1 , FontStrikeout1 , PhoneOrderPosition , AutoPopSpellInstructionKeyboard , KitchenScreen1 , KitchenScreen2 , KitchenScreen3 , KitchenScreen4 , Scalable , WeekendPrice , WeekendPrice1 , WeekendPrice2 , WeekendPrice3 , PicturePath , Description3 , Description4 , TimeChargeItem , SoldOut , PromotionItem , CanBeRedeemItem , TareWeight , Cost , Cost1 , Cost2 , Cost3 , QuantityFollowByPeopleCount , RedeemPoints , OnlineOrderItem , OtherChargeItem , WeightDivideMeasureAsQty , MeasureWeight , PId , ItemDescription1 , ItemDescription2 , PackagePrice , PackagePrice1 , PackagePrice2 , PackagePrice3 , NoteGroupCode , BorderColor , PictureCloudAddr , SubCategory , ItemDescription3 , ItemDescription4 , MaximumQty , TimeConsumingItem , OnlineStatus , QRCodeStatus , OnlinePrice1 , OnlinePrice2 , OnlinePrice3 , OnlinePrice4 , OnlinePicturePath , OnlinePictureCloudAddr , OnlineDisplayName1 , OnlineDisplayName2 , STRFTIME('%Y-%m-%d %H:%M:%S', SoldOutUpdateTime) as SoldOutUpdateTime   , StockControl , StockQty , DVersion , Version , MenuVersion , AllowGift , DoNotAutoEnterSubmenuPage , SoldOutSyncFlag , XeroAccountCode , XeroAccountId FROM MenuItem" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
          SQLData["Price"] = pd.to_numeric(SQLData["Price"] )
          SQLData["Price1"] = pd.to_numeric(SQLData["Price1"])
          SQLData["Price2"] = pd.to_numeric(SQLData["Price2"])
          SQLData["Price3"] = pd.to_numeric(SQLData["Price3"])
          
          SQLData["HappyHourPrice1"] = pd.to_numeric(SQLData["HappyHourPrice1"])
          SQLData["HappyHourPrice2"] = pd.to_numeric(SQLData["HappyHourPrice2"])
          SQLData["HappyHourPrice3"] = pd.to_numeric(SQLData["HappyHourPrice3"])
          SQLData["HappyHourPrice4"] = pd.to_numeric(SQLData["HappyHourPrice4"])
          
          SQLData["WeekendPrice"] = pd.to_numeric(SQLData["WeekendPrice"])
          SQLData["WeekendPrice1"] = pd.to_numeric(SQLData["WeekendPrice1"])
          SQLData["WeekendPrice2"] = pd.to_numeric(SQLData["WeekendPrice2"])
          SQLData["WeekendPrice3"] = pd.to_numeric(SQLData["WeekendPrice3"])
          
          SQLData["PackagePrice"] = pd.to_numeric(SQLData["PackagePrice"] )
          SQLData["PackagePrice1"] = pd.to_numeric(SQLData["PackagePrice1"] )
          SQLData["PackagePrice2"] = pd.to_numeric(SQLData["PackagePrice2"] )
          SQLData["PackagePrice3"] = pd.to_numeric(SQLData["PackagePrice3"] )
          
          SQLData["Cost"] = pd.to_numeric(SQLData["Cost"] )
          SQLData["Cost1"] = pd.to_numeric(SQLData["Cost1"] )
          SQLData["Cost2"] = pd.to_numeric(SQLData["Cost2"] )
          SQLData["Cost3"] = pd.to_numeric(SQLData["Cost3"] )
          
          SQLData["OnlinePrice1"] = pd.to_numeric(SQLData["OnlinePrice1"] )
          SQLData["OnlinePrice2"] = pd.to_numeric(SQLData["OnlinePrice2"] )
          SQLData["OnlinePrice3"] = pd.to_numeric(SQLData["OnlinePrice3"] )
          SQLData["OnlinePrice4"] = pd.to_numeric(SQLData["OnlinePrice4"] )

          
          
          
          writeToSQLFileLineByLine(TableName,SQLData)
          writeToExcelFile(TableName,SQLData) 
        












def processTable_MenuItemRelation(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "MenuItemRelation"
    Query = "SELECT PId , ItemCode , LinkItemCode , RelateItemCode , BuzId , Version , MenuVersion FROM MenuItemRelation" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        








def processTable_PresetNote(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "PresetNote"
    Query = "SELECT BuzId , Notes1 , Notes2 , Active , NoteGroupCode , OrderIndex , PId , Notes3 , Notes4 , Version , MenuVersion FROM PresetNote" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        





def processTable_SubItemGroup(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "SubItemGroup"
    Query = "SELECT SubGroupCode , SubGroupName1 , SubGroupName2 , PId , SubGroupName3 , SubGroupName4 , Version , MenuVersion FROM SubItemGroup" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        






def processTable_SubMenuLinkDetail(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "SubMenuLinkDetail"
    Query = "SELECT ItemCode , SubMenuCode , ChoiceItem , SalesPrice , Instruction , MaximunCharge , SalesQty , PId , OrderIndex , MultiPrice , IsDefault , DefaultPriceKind , Version , MenuVersion FROM SubMenuLinkDetail" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        






def processTable_SubMenuLinkHead(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "SubMenuLinkHead"
    Query = "SELECT ItemCode , SubCategory , AutoShowSubMenu , NumberOfChoice , PId , MinNumberOfChoice , Version , MenuVersion FROM SubMenuLinkHead" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        






def processTable_PresetNoteGroup(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "PresetNoteGroup"
    Query = "SELECT NoteGroupCode , NoteGroupName1 , NoteGroupName2 , PId , NoteGroupName3 , NoteGroupName4 , Version , MenuVersion FROM PresetNoteGroup;" 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        


















# Menu Data
# Category
# CategoryMenuItem
# course
# InstructionLink
# InstructionLinkGroup
# ItemGroupTable
# MenuGroupLinkCategory
# MenuGroupTable
# MenuGroupTimes
# MenuItem
# MenuItemRelation
# PresetNote
# PresetNoteGroup
# SubItemGroup
# SubMenuLinkDetail
# SubMenuLinkHead






























def processTable_OOOOO(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    TableName = "ooooo"
    Query = "   " 
    
    SQLData = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SQLData)
    if QuerySize>0:
       
        writeToSQLFileLineByLine(TableName,SQLData)
        writeToExcelFile(TableName,SQLData) 
        














def convertTOSQLServerProcess(SqliteDBFilePath):
    
    
    
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    initSingleSQLFile()
    #------------ Settings-----------------------
    processAssessMenuTable(SqliteDBFilePath)
    processChargeScopeTable(SqliteDBFilePath)
    processDiscountRateTableTable(SqliteDBFilePath)
    processDiscountSchemaTable(SqliteDBFilePath)
    processDrawerDeviceTable(SqliteDBFilePath)
    processMachineIDTable(SqliteDBFilePath)
    processPaymentTable(SqliteDBFilePath)
    processPrintConditionTable(SqliteDBFilePath)
    processPrinterDeviceTable(SqliteDBFilePath)
    processPrinterDeviceItemTable(SqliteDBFilePath)
    processProfileTable(SqliteDBFilePath)
    processSequenceIDTable(SqliteDBFilePath)
    processTablePageTable(SqliteDBFilePath)
    processTableSetTable(SqliteDBFilePath)

    processEftMachinePairTable(SqliteDBFilePath)
    
    processSysparameterTable(SqliteDBFilePath)
    processspecialdaytableTable(SqliteDBFilePath)
    #processTable_Category(SqliteDBFilePath)
    
    #--------------Menu---------------------------------
    processTable_Category(SqliteDBFilePath)
    processTable_CategoryMenuItem(SqliteDBFilePath)
    processTable_course(SqliteDBFilePath)
    processTable_InstructionLink(SqliteDBFilePath)
    processTable_InstructionLinkGroup(SqliteDBFilePath)
    processTable_ItemGroupTable(SqliteDBFilePath)
    processTable_MenuGroupLinkCategory(SqliteDBFilePath)
    processTable_MenuGroupTable(SqliteDBFilePath)
    processTable_MenuGroupTimes(SqliteDBFilePath)
    processTable_MenuItem(SqliteDBFilePath)
    processTable_MenuItemRelation(SqliteDBFilePath)
    processTable_PresetNote(SqliteDBFilePath)
    processTable_PresetNoteGroup(SqliteDBFilePath)
    processTable_SubItemGroup(SqliteDBFilePath)
    processTable_SubMenuLinkDetail(SqliteDBFilePath)
    processTable_SubMenuLinkHead(SqliteDBFilePath)
    
    completeSingleSQLFile()
    
    
    #-----------Business Data, Take looong time-------------
    processRecvAcctTable(SqliteDBFilePath)
    processOrderHTable(SqliteDBFilePath)
    processOrderITable(SqliteDBFilePath)
    
    
    
    mess="Process Complete please check " + directory
    
    messagebox.showinfo(title="info", message=mess)
    
            





def SqliteProcess(DBSource):
    SqliteDBconnection = sqlite3.connect(DBSource)
   
    connectionTestResult=0
    if DBSource=="":
        messagebox.showerror(title="Error", message="DB Name Field is Empty!!")
        connectionTestResult = 0
    else:
        
        try:
            SqliteDBconnection.cursor()
            connectionTestResult=1
        except Exception as ex:
        
            connectionTestResult=0
    
        
     
    if connectionTestResult==1:
        SqliteDBconnection.close()
        print("next")
        convertTOSQLServerProcess(DBSource)
        
        #processProductWithBarCode(connect_string)

    else:
        print("error")


# def ConnectionTest(connect_string):
#     connectionTestResult = 0
   
#     PassSQLServerConnection = pyodbc.connect(connect_string)

#     print(connect_string)
#     try:
#         PassSQLServerConnection = pyodbc.connect(connect_string)
#         print("{c} is working".format(c=connect_string))
#         PassSQLServerConnection.close()
#         connectionTestResult = 1
#     except pyodbc.Error as ex:
#         #print("{c} is not working".format(c=connect_string))
#         messagebox.showerror(title="Error", message="{c} is not working")

#     return connectionTestResult




# def inforProcess(SqliteSource,DBName):
#     connectionTestResult=0
#     #connect_string = 'DRIVER={SQL Server}; SERVER='+DBSource+'; DATABASE='+DBName+'; UID='+DBUsername+'; PWD='+ DBPassword
#     connect_string = 'DRIVER={SQL Server}; SERVER='+DBSource+'; DATABASE='+DBName+'; Trusted_Connection=yes;'
    
    
    
#     if DBName=="":
#         messagebox.showerror(title="Error", message="DB Name Field is Empty!!")
#         connectionTestResult = 0
#     else:
#         connectionTestResult=ConnectionTest(connect_string)

#     if connectionTestResult==1:
#         print("next")
        

#     else:
#         print("error")


class App:
    def __init__(self, root):
        #setting title
        root.title("ZiiPOS Sqlite TO SQL Server Converter")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        
        SQLITEGLabel_DB_Source=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        SQLITEGLabel_DB_Source["font"] = ft
        SQLITEGLabel_DB_Source["fg"] = "#333333"
        SQLITEGLabel_DB_Source["justify"] = "left"
        SQLITEGLabel_DB_Source["text"] = "Sqlite DB File"
        SQLITEGLabel_DB_Source.place(x=50,y=100,width=90,height=30)
        
        SQLITDBSource_Box=tk.Entry(root)
        SQLITDBSource_Box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        SQLITDBSource_Box["font"] = ft
        SQLITDBSource_Box["fg"] = "#333333"
        SQLITDBSource_Box["justify"] = "left"
        #DBSource_Box.insert(0,'SelectSqliteFile')
        SQLITDBSource_Box.place(x=190,y=100,width=205,height=30)
        
        
        

        # GLabel_DB_Source=tk.Label(root)
        # ft = tkFont.Font(family='Times',size=10)
        # GLabel_DB_Source["font"] = ft
        # GLabel_DB_Source["fg"] = "#333333"
        # GLabel_DB_Source["justify"] = "left"
        # GLabel_DB_Source["text"] = "DB Connection"
        # GLabel_DB_Source.place(x=50,y=90,width=90,height=30)

        # DBSource_Box=tk.Entry(root)
        # DBSource_Box["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # DBSource_Box["font"] = ft
        # DBSource_Box["fg"] = "#333333"
        # DBSource_Box["justify"] = "left"
        # DBSource_Box.insert(0,'localhost\\sqlexpress2008r2')
        # DBSource_Box.place(x=190,y=90,width=205,height=30)
        
        
        # DB_UserName_Label=tk.Label(root)
        # ft = tkFont.Font(family='Times',size=10)
        # DB_UserName_Label["font"] = ft
        # DB_UserName_Label["fg"] = "#333333"
        # DB_UserName_Label["justify"] = "left"
        # DB_UserName_Label["text"] = "User Name"
        # DB_UserName_Label.place(x=50,y=140,width=90,height=30)

        # DB_UserName_Box=tk.Entry(root)
        # DB_UserName_Box["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # DB_UserName_Box["font"] = ft
        # DB_UserName_Box["fg"] = "#333333"
        # DB_UserName_Box["justify"] = "left"
        # #DB_UserName_Box["text"] = "sa"
        # DB_UserName_Box.insert(0,'sa')
        # DB_UserName_Box.place(x=190,y=140,width=275,height=30)

        # DB_Password_Label=tk.Label(root)
        # ft = tkFont.Font(family='Times',size=10)
        # DB_Password_Label["font"] = ft
        # DB_Password_Label["fg"] = "#333333"
        # DB_Password_Label["justify"] = "left"
        # DB_Password_Label["text"] = "Password"
        # DB_Password_Label.place(x=50,y=200,width=90,height=25)

        # DB_Password_Box=tk.Entry(root)
        # DB_Password_Box["borderwidth"] = "1px"
        
        # ft = tkFont.Font(family='Times',size=10)
        # DB_Password_Box["font"] = ft
        # DB_Password_Box["fg"] = "#333333"
        # DB_Password_Box["justify"] = "left"
        # #DB_Password_Box["text"] = "0000"
        # DB_Password_Box.insert(0,'0000')
        # DB_Password_Box.place(x=190,y=200,width=275,height=30)
        # DB_Password_Box["show"] = "*"

        
        
        # DB_Name_Label=tk.Label(root)
        # ft = tkFont.Font(family='Times',size=10)
        # DB_Name_Label["font"] = ft
        # DB_Name_Label["fg"] = "#333333"
        # DB_Name_Label["justify"] = "left"
        # DB_Name_Label["text"] = "DB Name"
        # DB_Name_Label.place(x=50,y=260,width=90,height=25)

        # DB_Name_Box=tk.Entry(root)
        # DB_Name_Box["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # DB_Name_Box["font"] = ft
        # DB_Name_Box["fg"] = "#333333"
        # DB_Name_Box["justify"] = "left"    
        # DB_Name_Box.place(x=190,y=260,width=275,height=30)
        # DB_Name_Box.insert(0,'ZiiPOS')

      








         #-----------------Functions---------------------------------
        def getSqliteDBSource():
            
            result=SQLITDBSource_Box.get()
            return result
        
        
        # def createSqlFileCheck():
        #     result=CreateSQLBox.CreateSQLBoxVariable.get()
        #     print(result)
        #     createSQLFileCheckFlag=result
       
        
        # def createExcelFileCheck():
        #     result=CreateExcelBox.CreateExcelBoxVariable.get()
        #     print(result)
        #     createExcelFileCheckFlag= result
        
        # def getDBSource():
        #     result=DBSource_Box.get()
        #     return result
           
            
        # def getDBUsername():
        #     result=DB_UserName_Box.get()
        #     return result
      
        # def getDBPassword():
        #     result=DB_Password_Box.get()
        #     return result
        
        # def getDBName():
        #     result=DB_Name_Box.get()
        #     return result
      
        
        # def StartConversionProcess():
        #     SqliteDB=getSqliteDBSource()
            
            
        #     DBSource=getDBSource()
        #     username=getDBUsername()
        #     password=getDBPassword()
        #     databaseName=getDBName()
            
        #     inforProcess(SqliteDB,DBSource,username,password,databaseName)
        #     inforProcess(DBSource,databaseName)
            
        #def getCheckBox:
            

        # def testDBSource():
        #     DBSource=getDBSource()
        #     username=getDBUsername()
        #     password=getDBPassword()
        #     databaseName=getDBName()
           
        #     if databaseName=="":
        #         messagebox.showerror(title="Error", message="DB Name Field is Empty!!")
        #     else:
                
        #         connect_string = 'DRIVER={SQL Server}; SERVER='+DBSource+'; DATABASE='+databaseName+'; UID='+username+'; PWD='+ password
        #         #connect_string = 'DRIVER={SQL Server}; SERVER='+DBSource+'; DATABASE='+databaseName+'; Trusted_Connection=yes;'
        #         PassSQLServerConnection = pyodbc.connect(connect_string)
                
        #         try:
        #             messagebox.info(title="info", message="DB is working")
        #             PassSQLServerConnection = pyodbc.connect(connect_string)
        #             print("{c} is working".format(c=connect_string))
        #             PassSQLServerConnection.close()
        #         except pyodbc.Error as ex:
        #             messagebox.showerror(title="Error", message="DB is not working")
        #             print("{c} is not working".format(c=connect_string))
                    

        
        def StartConversionProcess():
           
            SqliteFile=getSqliteDBSource()
            SqliteProcess(SqliteFile)
            

        def SelectDBFile():
            #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            print(filename)
            SQLITDBSource_Box.insert(0,filename)
            SqliteFilePath=filename
          
            




            
            


            
            
        
        
        

            














#-------------------------------------------------------
        # CreateSQLBox=tk.Checkbutton(root)
        # ft = tkFont.Font(family='Times',size=10)
        # CreateSQLBox["font"] = ft
        # CreateSQLBox["fg"] = "#333333"
        # CreateSQLBox["justify"] = "center"
        # CreateSQLBox["text"] = "Export To SQL File"
        # CreateSQLBox.place(x=90,y=340,width=150,height=25)
        # CreateSQLBox["offvalue"] = "0"
        # CreateSQLBox["onvalue"] = "1"
        # CreateSQLBox["variable"] = "CreateSQLBoxVariable"
        # CreateSQLBox.select()
        # #CreateSQLBox["command"] = self.CreateSQLBox_command

        # CreateExcelBox=tk.Checkbutton(root)
        # ft = tkFont.Font(family='Times',size=10)
        # CreateExcelBox["font"] = ft
        # CreateExcelBox["fg"] = "#333333"
        # CreateExcelBox["justify"] = "center"
        # CreateExcelBox["text"] = "Export To Excel"
        # CreateExcelBox.place(x=260,y=340,width=150,height=25)
        # CreateExcelBox["offvalue"] = "0"
        # CreateExcelBox["onvalue"] = "1"
        # CreateExcelBox["variable"] = "CreateExcelBoxVariable"
        # CreateExcelBox.select()
        # #CreateExcelBox["command"] = self.CreateExcelBox_command

        # InsertToSQLServerBox=tk.Checkbutton(root)
        # ft = tkFont.Font(family='Times',size=10)
        # InsertToSQLServerBox["font"] = ft
        # InsertToSQLServerBox["fg"] = "#333333"
        # InsertToSQLServerBox["justify"] = "center"
        # InsertToSQLServerBox["text"] = "Insert to SQL Server"
        # InsertToSQLServerBox.place(x=410,y=340,width=150,height=25)
        # InsertToSQLServerBox["offvalue"] = "0"
        # InsertToSQLServerBox["onvalue"] = "1"
        #InsertToSQLServerBox["command"] = self.InsertToSQLServerBox_command
        



            
#--------------Button Actions-------------------------


        SelectDBFile_Button=tk.Button(root)
        SelectDBFile_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        SelectDBFile_Button["font"] = ft
        SelectDBFile_Button["fg"] = "#000000"
        SelectDBFile_Button["justify"] = "center"
        SelectDBFile_Button["text"] = "Select SqliteDB"
        SelectDBFile_Button.place(x=410,y=100,width=110,height=30)
        SelectDBFile_Button["command"] = SelectDBFile
        #DBSource_Box.place(x=190,y=90,width=205,height=30)
        
        Star_Button=tk.Button(root)
        Star_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Star_Button["font"] = ft
        Star_Button["fg"] = "#000000"
        Star_Button["justify"] = "center"
        Star_Button["text"] = "Start"
        Star_Button.place(x=70,y=390,width=90,height=45)
        Star_Button["command"] = StartConversionProcess

      
        
        # TEST_Button=tk.Button(root)
        # TEST_Button["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # TEST_Button["font"] = ft
        # TEST_Button["fg"] = "#000000"
        # TEST_Button["justify"] = "center"
        # TEST_Button["text"] = "Test DB"
        # TEST_Button.place(x=250,y=390,width=90,height=45)
        # TEST_Button["command"] = testDBSource

        Close_Button=tk.Button(root)
        Close_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Close_Button["font"] = ft
        Close_Button["fg"] = "#000000"
        Close_Button["justify"] = "center"
        Close_Button["text"] = "Close"
        Close_Button.place(x=420,y=390,width=90,height=45)
        Close_Button["command"] = closesystem
       
        




#----------------Not in use--------------------------------
    def Star_Button_command(self):
        print("Star_Button_command")
    def SelectDBFile_Button_command(self):
        print("command")
    def Close_Button_command(self):
        print("Exit")
        exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
