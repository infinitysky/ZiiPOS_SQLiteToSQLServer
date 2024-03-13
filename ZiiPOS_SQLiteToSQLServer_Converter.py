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

from tqdm import tqdm


ssl._create_default_https_context = ssl._create_unverified_context


directory='C:\\Ziitech'


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
    sql = f"insert into {tableName} ({cols}) values {f_values};" 

    print(sql)   

    fileName=directory+'\\'+tableName +'.sql'
   
    if os.path.exists(fileName):
        os.remove(fileName)
        
    else:
        f = open(fileName, "a")
        f.write("delete from "+tableName+" ; \n")
        f.write("SET IDENTITY_INSERT "+ tableName+" ON; \n")
        f.write(sql)
        f.write("\nSET IDENTITY_INSERT "+ tableName+" OFF;\n")
        f.close()
        



def processAssessMenuTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT  AuthoriseCloseWindow,AuthoriseDiscount,BookingFormConditionSetupMenu,DailyReportMenu,DatabaseBackupMenu,DatabaseRestoreMenu,InvoiceConditionSetupMenu,OpenCashDrawerMenu,PaymentAuthority,PrintInvoiceAuthority,PrintJobListAuthority,TableInformationSetupMenu,StaffName,SecureCode,Supervisor,BookingListMenu,StockReceiveMenu,InquirySalesHistoryMenu,VIPInformationMenu,SalesReportMenu,SalesStatisticsReportMenu,StockReportMenu,StockReceiveReportMenu,StatisticsChartMenu,SupplierInformationListMenu,ExpensesDescriptionSetupMenu,ExpensesDataEntryMenu,ExpensesReportMenu,ReceiptsReportMenu,PaymentsReportMenu,GSTPayableReportMenu,ProfileSetupMenu,PrinterSetupMenu,CategorySetupMenu,MenuSetupMenu,PaymentsMethodSetupMenu,SupplierInformationSetupMenu,Birthday,Telephone,Mobile,Fax,Address,Rate,AttendanceReportMenu,VoidItemAuthority,PurchaseOrderMenu,PurchasePayableMenu,TableOrderMenu,PointOfSalesMenu,CheckDailyReport,AuthoriseRefund,UserManager,AllowEditOrder,PrintDailyReport,DrawerPortNumber,DefaultDrawerPortNumber,EditAttendanceRecord,StockAdjustmentMenu,StockAdjustmentReportMenu,PhoneOrderMenu,CashPayOutMenu,CashFloatMenu,AssignDriverAuthorised,DepositMenu,WastageMenu,WastageReportMenu,AuthrisedCancelHoldOrder,ManuallyEnterDiscountRate,EditOrderPayment,InquirySalesRelatedReportDays,CashDeclarationReportMenu,AccountEnabled,AuthorizedChangeQty,AuthorizedChangePrice,DeleteVIPRecord,ControlButtonSetup,DiscountRateSetup,VoidItemDescriptionSetup,EFTPOSUtility,ChangeMenuStatus,StockTakeMenu,StockTakeReportMenu,UserGroupSetupAuthorized,UploadMembersRewardsMenu,PId,SettingsPortalMenu,ZiiTOTableLockMenu,StaffCode,FirstName,LastName,ZiiOnlineOrderCancel,OverrideSalesPrice, STRFTIME('%Y-%m-%d %H:%M:%S', LastUpdatedTime) as LastUpdatedTime  FROM AccessMenu;"
    
   
    AccessMenu = pd.read_sql_query(Query, Connection)

   
    Connection.close()
    
    
    QuerySize = len(AccessMenu)
    if QuerySize>0:
        writeToSQLFile("AccessMenu",AccessMenu)
        Export_file=directory+"\\AccessMenu.xlsx"
        AccessMenu.to_excel(Export_file, index = True, header=True,engine='xlsxwriter')
    
    


def processDiscountRateTableTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Description, DiscountRate,DiscountKind,PId FROM DiscountRateTable;" 
    DiscountRateTable = pd.read_sql_query(Query, Connection)
        
    Connection.close()
    
    QuerySize = len(DiscountRateTable)
    if QuerySize>0:
        writeToSQLFile("DiscountRateTable",DiscountRateTable)
        Export_file=directory+"\\DiscountRateTable.xlsx"
        DiscountRateTable.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
    
    
      


def processDiscountSchemaTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT SchemaCode, SchemaName,Rate,Kind,Active,CreateBy,STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt FROM DiscountSchema;" 
    DiscountSchema = pd.read_sql_query(Query, Connection)
             
    
    Connection.close()
    
    
    QuerySize = len(DiscountSchema)
    if QuerySize>0:
        writeToSQLFile("DiscountSchema",DiscountSchema)
        Export_file=directory+"\\DiscountSchema.xlsx"
        DiscountSchema.to_excel(Export_file, index = True, header=True,engine='xlsxwriter')   
    
   
    
    
    
    

def processChargeScopeTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT ChargeRate,Model,Frequency,StartTime,EndTime,ApplyOnDineIn,ApplyOnTakeaway,ApplyOnQuickSale,ApplyOnDelivery,ApplyOnPickup,STRFTIME('%Y-%m-%d %H:%M:%S', CreatedAt) as  CreatedAt, STRFTIME('%Y-%m-%d %H:%M:%S', UpdatedAt) as UpdatedAt ,PId FROM ChargeScope" 
    ChargeScope = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(ChargeScope)
    if QuerySize>0:
        writeToSQLFile("ChargeScope",ChargeScope)
        Export_file=directory+"\\ChargeScope.xlsx"
        ChargeScope.to_excel(Export_file, index = True, header=True,engine='xlsxwriter')    
      
        


   

def processDrawerDeviceTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,DrawerNo,ConnectToNo,Speed,PinModel,CheckStatus,DrawerMode,Enabled,Description FROM DrawerDevice" 
    
    DrawerDevice = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(DrawerDevice)
    if QuerySize>0:
        Export_file=directory+"\\DrawerDevice.xlsx"
        DrawerDevice.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("DrawerDevice",DrawerDevice)
        


def processMachineIDTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    
    Query = "SELECT MachineID,PId,DefaultCheckListPrinter,DefaultDrawerNo,Description,DefaultPrinter,ClientUniqueId,Disabled,STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt , STRFTIME('%Y-%m-%d %H:%M:%S', BindAt) as BindAt ,EnableEftposProduce,DefaultKitchenScreen,MachineType,IpAddress,FixedJobListPrinter FROM MachineID" 
    
    MachineID = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(MachineID)
    if QuerySize>0:
        Export_file=directory+"\\MachineID.xlsx"
        MachineID.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("MachineID",MachineID)
        

def processPaymentTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT ShowOnList,Payment,SurchargeRate,Code,EFTPOSPayment,LinkToDevice,PId,CounterPayment,SupportCasher,SupportSelfPad,OrderIndex,SupportOrderingTerminal,SpecialChargeRate,XeroAccountCode,XeroAccountId FROM Payment" 
    
    Payment = pd.read_sql_query(Query, Connection)
    Connection.close()
    QuerySize = len(Payment)
    if QuerySize>0:
        Export_file=directory+"\\Payment.xlsx"
        Payment.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("Payment",Payment)


def processPrintConditionTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,BillCondition,InvoiceCondition,BookingFormCondition,BuzId FROM PrintCondition" 
    
    PrintCondition = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(PrintCondition)
    if QuerySize>0:
        Export_file=directory+"\\PrintCondition.xlsx"
        PrintCondition.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("PrintCondition",PrintCondition)
        
        

def processPrinterDeviceTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,DefaultPrinterIDNo,MobileDefaultPrinterIDNo,CheckListPrinterIDNo,SupportChinese,PrintLogoOnPOSPrinter,FeedLinesBeforeCut,FeedLinesBeforePringJob,DefaultDrawerNo,IntegratedEFTReceipt,BuzId FROM PrinterDevice" 
    
    PrinterDevice = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(PrinterDevice)
    if QuerySize>0:
        Export_file=directory+"\\PrinterDevice.xlsx"
        PrinterDevice.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("PrinterDevice",PrinterDevice)
        
        
        
        
        
        
        
        
def processPrinterDeviceItemTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "  SELECT PId,PrinterNo,ModelType,PortType,PortSetting,PrinterName,TableOrderJobListTitle,QuickServiceJobListTitle,PhoneOrderJobListTitle,JobListDuplicate,GoWithMessage,SupportGraphic,Thermal,JobListCopies FROM PrinterDeviceItem" 
    
    PrinterDeviceItem = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(PrinterDeviceItem)
    if QuerySize>0:
        Export_file=directory+"\\PrinterDeviceItem.xlsx"
        PrinterDeviceItem.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("PrinterDeviceItem",PrinterDeviceItem)
        
                
def processProfileTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = " SELECT BeginTime,CheckPassword,EndTime,MainCategoryLine,MainMenuLine,NotAllowModify,POSCategoryLine,POSMenuLine,CompanyName,Telephone,Fax,ABN,Address,Initial,ButtonLayOut,ServiceChargeRate,TableTracking,PersonCount,CheckTableStatus,PrintBillNo,RoundingFlag,ForceVIPDiscount,AutoOpenTill,AutoPrintJobList,PrintServiceOnJobList,PrintPersonsOnJobList,PrintPriceOnJobList,PrintTimeOnInvoice,HappyHour,HappyHourStartTime,HappyHourEndTime,ShowTaxOnSalesSection,POSJobList,POSOrderList,POSInvoice,PrintPickupSlip,PrintCategoryColor,OrderListDescription,InvoiceDescription,PrintBillCategory,PrintInvoiceCategory,VIPDefaultSearch,AutoPrintPhoneOrderJobList,AutoInstructionSelection,PrintTableNo,PrintDateOnDailyReport,AutoPrintBill,AutoPrintInvoice,AutoPriceWindow,PrintZeroPriceItemOnInvoice,AutoPopVoidReason,ManuallyEnterTableNumber,PrintInvoiceNo,AutoSaveOrder,ScaleBarcode,PrintGoWithInstruction,PrintOpNameOnJobList,AutoPrintMergedOrder,AutoPrintJobListForHoldOrder,AutoSurcharge,SurchargeStartTime,SurchargeEndTime,HappyHourStartTime1,HappyHourEndTime1,HappyHourStartTime2,HappyHourEndTime2,HappyHourStartTime3,HappyHourEndTime3,HappyHourStartTime4,HappyHourEndTime4,HappyHourStartTime5,HappyHourEndTime5,HappyHourStartTime6,HappyHourEndTime6,SurchargeName,OtherCharge,OtherChargeName,OtherChargeRate,PriceIncludesGST,DefaultGSTRate,DefaultVIPState,PrintIngredientsOnJobList,MaxDiscountPercentage,MaxDollarDiscount,JobListFontSize,DefaultBackupPath,ShowPrintInvoiceWindow,ChangeQtyWithCondiment,CompulsoryEnterCustomerName,AutoPrintCheckList,PrintOrderNoOnJobList,AutoBackup,BackupTime,PhoneOrderMenuLine,PhoneOrderCategoryLine,ManuallyPrintJobList,PhoneOrderJobListFormat,BackupFrequency,BackupOnceTime,DiscountRateEnterMode,ShowNegativeQty,PrintOrderNoOnTaxInvoice,CheckListFormat,AutoLogout,AutoLogoutTimeOut,PrintRedColorQtyOnJobList,MinimumChargeKind,OnlyOpenDrawerForCashPayment,MinimumChargeItemCode,MinimumChargePerPerson,PrintDiscountRateOnBill,OnlyPrintSimpleFormatDailyReport,OnlyPrintLastTwoDigitalOrderNo,CheckPrinterStatus,AutoPrintBillWhenPhoneOrderSaved,AutoAddDeliveryChargeForPhoneOrder,DeliveryChargeItemCode,PrintZeroQtyItemsOnJobList,JobListFormatForPrinter1,JobListFormatForPrinter2,JobListFormatForPrinter3,JobListFormatForPrinter4,JobListFormatForPrinter5,JobListFormatForPrinter6,JobListFormatForPrinter7,JobListFormatForPrinter8,JobListFormatForPrinter9,JobListFormatForPrinter10,JobListFormatForPrinter11,JobListFormatForPrinter12,SecondDisplayDescription,ForceCashDeclaration,SubMenuStyle,RemindVIPBirthday,PrintOrderDateOnJobList,AutoWeightScalableItem,CheckListDescription,JobListRelateFormat,TableServiceJobListFormat,QuickServiceJobListFormat,PrintCustomerNameOnJobList,DoNotPrintVoidItemsOnJobList,PrintTableNumberChoice,EnableWeekendPriceFunction,WeekendPriceStartDay,WeekendPriceEndDay,SelfOrderConsole,KeepCancelSales,PrintSpellInstructionOnBill,PrintServicePeopleNameOnInvoice,PrintTotalOnCheckList,PrintCustomerDetailOnInvoice,DefaultPhoneOrderKind,CustomerNameEnterKeypad,PrintItemInRedForJobList,InstructionItemsPrintToOwnPrinters,PrintVoidItemOnDailyReport,PrintGroupSalesOnDailyReport,PrintNonSalesOpenDrawerOnDailyReport,EnableEatInTakeAwayFunction,AutoSetPhoneOrderDueTime,DefaultPhoneOrderDueTime,AutoIssueVoucher,VoucherSalesAmount,VoucherDescription,PromotionDiscountTerm,SubMenuSortBy,LoyaltyReward,RewardPointsRate,RedeemPointsRate,ConnectionKind,URL,RewardsKind,EnablePagerFunction,ElapseTimeKind,DoNotPrintVoidItemOnInvoice,KeypadButtonLinks,OnlyPrintNewItemOnCheckList,PrintReprintSymbolOnJobList,PrintOrderNumberOnInvoiceTop,PrintOrderNumberOnBillTop,DefaultServiceKind,ForceSelectPaymentMethod,BookingTableStatusKind,PrintAmountOnPickupSlip,EnterCustomerIDForHoldOrder,PrintConsolidatedItemsOnJobList,PrintTableMergeInformation,PrintSeatNumberOnJobList,PrintGratuityFillInSpaceOnBill,PrintSmallFontForInstructionItemOnJobList,PrintJobListAfterEachPayment,AutoPrintAttendanceSlip,DefaultStockItemSearch,ForceToOpenLockedTable,ForceOpenLockedTableWithComfirmInfo,JobListDescriptionforPrinter1,JobListDescriptionforPrinter2,JobListDescriptionforPrinter3,JobListDescriptionforPrinter4,JobListDescriptionforPrinter5,JobListDescriptionforPrinter6,JobListDescriptionforPrinter7,JobListDescriptionforPrinter8,JobListDescriptionforPrinter9,JobListDescriptionforPrinter10,JobListDescriptionforPrinter11,JobListDescriptionforPrinter12,JobListSecondDescription1,JobListSecondDescription2,JobListSecondDescription3,JobListSecondDescription4,JobListSecondDescription5,JobListSecondDescription6,JobListSecondDescription7,JobListSecondDescription8,JobListSecondDescription9,JobListSecondDescription10,JobListSecondDescription11,JobListSecondDescription12,UseOriginalItemPrice,SaturdayWageRate,SundayWageRate,PublicHolidayWageRate,ShowSeatNumberAsSpellInstruction,ForceSelectTakeAwayOrEatIn,DefaultCreditCardSurchargeRate,PrintPaymentDetail,JobListTimeFormat,ShowMemberIDOnOrderScreen,OnlyShowMemberFirstName,CheckVoucherIDViaInternet,GiftcardExpireDays,AutoPrintParkingVoucher,ResetMenuButtonForNewOrder,ChioceMenuGroupForiMenu,NotConsolidateForEachItemOnDifferentDockect,EnablePresetNotes,NotesAtJobListPosition,ShowNotesOnOrderForm,CalculateOtherChargeKind,SmallButtonForQuickSales,PaymentChangeForwardToTips,PrintCreditCardPaymentOption,EFTPOSPaymentSurchargeApplyToTips,ShowElapseTime,PId,DineInPriorityCheckout,SupportMultiLanguage,EnableDineIn,EnableTakeAway,EnableQuickService,LinkEFTPOSType,AutoSendJobListToScreen,KitchenScreenReminderTime,BuzId,EnableQuickCheckOut,EnableSpecialDay,BookingAccessKind,EnableDelivery,EnablePickUp,OrderTypeFirstChoice,PrintCourseItemVerbally,PrintCourseAndSendIfNeed,PrintCourseWhenCalled,PrintConsolidatedItemsOnInvoiceBill,TableTimeLimit,PrintMembershipQrcodeOnBill,PrintMembershipDescriptionOnBill,OrderItemNoteEnabled,OrderNoteEnabled,PrintPickNoOnCheckList,PrintOnlineNoOnJobList,PrintOrderNoOnLableJobList,PrintOnlineNoOnInvoiceBill,PrintConsolidatedInstructionsOnJobList,PrintConsolidatedInstructionsOnInvoiceBill,NotConsolidateForEachInsOnDifferentDockect,AutoPrintTakeAwayJobList,AutoPrintTakeAwayBill,AutoPrintTakeAwayInvoice,AutoPrintPickUpJobList,AutoPrintPickUpBill,AutoPrintPickUpInvoice,AutoPrintDeliveryJobList,AutoPrintDeliveryBill,AutoPrintDeliveryInvoice,PrintCopiesQtyOnJobList,QRCodePayType,PrintCustNameInsteadOnLabelJobList,SplitPrintMultiOrdered FROM Profile" 
    
    Profile = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(Profile)
    if QuerySize>0:
        Export_file=directory+"\\Profile.xlsx"
        Profile.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("Profile",Profile)
        
        
        
        
def processSequenceIDTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT SequenceId,ItemCode,NowNumber   FROM SequenceID" 
    
    SequenceID = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(SequenceID)
    if QuerySize>0:
        Export_file=directory+"\\SequenceID.xlsx"
        SequenceID.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("SequenceID",SequenceID)
        


def processTablePageTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PageNo,Description,PId   FROM TablePage " 
    
    TablePage = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(TablePage)
    if QuerySize>0:
        Export_file=directory+"\\TablePage.xlsx"
        TablePage.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("TablePage",TablePage)
        
        
        

def processTableSetTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Status,TableNo,Seats,FontName,FontSize,FontBold,FontItalic,FontUnderline,FontStrikeout,ButtonShape,ButtonWidth,ButtonHeight,ButtonX,ButtonY,PropertyFlag,Description,PageFlag,PDAPosition,MinimumChargePerTable,ServiceStatus,IPAddress,SelfOrderStatus,TerminalConnected,TableLockerName,OnlineOrderTable,PId,ZiiTOTableLockName,TeamNo, STRFTIME('%Y-%m-%d %H:%M:%S', LockUpdateTime) as LockUpdateTime , STRFTIME('%Y-%m-%d %H:%M:%S', TeamLocalTime) as TeamLocalTime  FROM TableSet" 
    
    #STRFTIME('%Y-%m-%d %H:%M:%S', BindAt) as BindAt
    
    TableSet = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(TableSet)
    if QuerySize>0:
        Export_file=directory+"\\TableSet.xlsx"
        TableSet.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("TableSet",TableSet)
        

def processRecvAcctTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Transfer,OrderNo, STRFTIME('%Y-%m-%d %H:%M:%S', AccountDate) as AccountDate ,PaidAmount,Payby,IDNo,OpName,MachineID,DepositID,GiftCardBalance, STRFTIME('%Y-%m-%d %H:%M:%S', GiftCardExpireDate) as GiftCardExpireDate ,Notes,PId,Surcharge,Tips,PaymentFlag,RelatedRecvID,PaymentActivityBuzId,SpecialCharge FROM RecvAcct" 
    
    RecvAcct = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(RecvAcct)
    if QuerySize>0:
        Export_file=directory+"\\RecvAcct.xlsx"
        RecvAcct.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("RecvAcct",RecvAcct)
        

def processOrderHTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT BookingNo,Credit,OrderPrinted,Tips,STRFTIME('%Y-%m-%d %H:%M:%S', OrderDate) as OrderDate  ,OrderNo,Persons,TableNo,ServicePerson,Amount,GST,PaidAmount,InvoiceNo,VIPNo,OpName,ServiceCharge,ServiceChargeRate,Surcharge,MachineID,BillKind,DollarDiscount, STRFTIME('%Y-%m-%d %H:%M:%S', DueTime) as DueTime,DiscountKind,Delivery,OtherCharge,OtherChargeRate,PriceIncludesGST,CurrentGSTRate,SplitBill,CustomerName,DiscountOperator,MemberID,CurrentPoints,CustomerAddress,CustomerTelephone,PointsUploaded,AwardEffective,PresetDiscountCode,VoucherID,VoucherAmount,VoucherDiscount,RedeemPoints,TotalRedeemPoints,SelfOrderMenuGroup,Notes,PId,SourceType,SourceKind,PackageCharge, STRFTIME('%Y-%m-%d %H:%M:%S', CheckoutCompleteTime) as CheckoutCompleteTime ,DeliveryFee,PayAfterDinner,OnlineOrderId, STRFTIME('%Y-%m-%d %H:%M:%S', BuzUpdateAt) as BuzUpdateAt ,STRFTIME('%Y-%m-%d %H:%M:%S', EndDueTime) as EndDueTime , STRFTIME('%Y-%m-%d %H:%M:%S', HoldTime) as HoldTime ,SourceOrderType,TeamNo,TeamTables,PayMode,ChannelOrderDisplayId,Channel,SpecialCharge,Kids,ManualServiceChargeRate,ExperienceFlag,PendingOrder,NotifyStatus, STRFTIME('%Y-%m-%d %H:%M:%S', NotifyAt) as NotifyAt ,CrmSeq,GuestId,DropFraction   FROM OrderH" 
    
    OrderH = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(OrderH)
    if QuerySize>0:
        Export_file=directory+"\\OrderH.xlsx"
        OrderH.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("OrderH",OrderH)
        

def processOrderITable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT Condition,PaidQty,PriceSelect,Seat,OrderNo,ItemCode,Qty,Price,Discount,TaxRate,IDNo,PrintFlag,SentToKitchen,VoidReason,SpecialOrder,CheckListPrinted,VoidFlag,OrderOperator,OriginalPrice,PresetDiscountCode,OriginalQty,RedeemItem,ManuallyEnterWeight,PId,RedeemPoints,PackagePrice,SeatNumber,CourseCode,CourseSendFlag,OtherChargeItem,OrderIndex,OnlineItemId,STRFTIME('%Y-%m-%d %H:%M:%S', CreateAt) as CreateAt ,BatchNumber,ParentItemCode,ParentSerialNo,SerialNo,SourceSerialNo, STRFTIME('%Y-%m-%d %H:%M:%S', BuzUpdateAt) as BuzUpdateAt  ,CoursePrintFlag,ServiceName,ServiceCode,CategoryCode,GiftFlag,AllowGift,Scalable,TareWeight,SourceIdNo,WasteInfo,OrderFrequency,ItemFrequency,STRFTIME('%Y-%m-%d %H:%M:%S', PendingEndAt) as PendingEndAt ,PendingFlag,LastBatchNumber   FROM OrderI" 
    
    OrderI = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(OrderI)
    if QuerySize>0:
        Export_file=directory+"\\OrderI.xlsx"
        OrderI.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("OrderI",OrderI)
        
        
                
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

def processOOOOOOOOTable(SqliteDBFilePath):
    Connection = sqlite3.connect(SqliteDBFilePath)
    Query = "SELECT PId,DrawerNo,ConnectToNo,Speed,PinModel,CheckStatus,DrawerMode,Enabled,Description FROM DrawerDevice" 
    
    DrawerDevice = pd.read_sql_query(Query, Connection)
    Connection.close()
  
    QuerySize = len(DrawerDevice)
    if QuerySize>0:
        Export_file=directory+"\\DrawerDevice.xlsx"
        DrawerDevice.to_excel(Export_file, index = True, header=True,engine='xlsxwriter') 
        writeToSQLFile("DrawerDevice",DrawerDevice)
        




def convertTOSQLServerProcess(SqliteDBFilePath):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
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
    processRecvAcctTable(SqliteDBFilePath)
    processOrderHTable(SqliteDBFilePath)
    processOrderITable(SqliteDBFilePath)
    
    
    messagebox.showinfo(title="info", message="Process Complete")
    
            






def infoProcess(DBSource):
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

        GLabel_DB_Source=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_DB_Source["font"] = ft
        GLabel_DB_Source["fg"] = "#333333"
        GLabel_DB_Source["justify"] = "left"
        GLabel_DB_Source["text"] = "DB Connection"
        GLabel_DB_Source.place(x=50,y=90,width=90,height=30)

        DBSource_Box=tk.Entry(root)
        DBSource_Box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        DBSource_Box["font"] = ft
        DBSource_Box["fg"] = "#333333"
        DBSource_Box["justify"] = "left"
        #DBSource_Box.insert(0,'SelectSqliteFile')
        DBSource_Box.place(x=190,y=90,width=205,height=30)

      








         #-----------------Functions---------------------------------
        def getDBSource():
            result=DBSource_Box.get()
            
            return result

        
        def StartConversionProcess():
            DBSource=getDBSource()
            infoProcess(DBSource)
            

        def SelectDBFile():
            #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            print(filename)
            DBSource_Box.insert(0,filename)
            SqliteFilePath=filename
          
            




            
            


            
            
        
        
        

            















        



            
#--------------Button Actions-------------------------
        Star_Button=tk.Button(root)
        Star_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Star_Button["font"] = ft
        Star_Button["fg"] = "#000000"
        Star_Button["justify"] = "center"
        Star_Button["text"] = "Start"
        Star_Button.place(x=70,y=390,width=90,height=45)
        Star_Button["command"] = StartConversionProcess

        TEST_Button=tk.Button(root)
        TEST_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        TEST_Button["font"] = ft
        TEST_Button["fg"] = "#000000"
        TEST_Button["justify"] = "center"
        TEST_Button["text"] = "Select SqliteDB"
        TEST_Button.place(x=410,y=90,width=110,height=30)
        TEST_Button["command"] = SelectDBFile
        #DBSource_Box.place(x=190,y=90,width=205,height=30)

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
    def TEST_Button_command(self):
        print("command")
    def Close_Button_command(self):
        print("Exit")
        exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
