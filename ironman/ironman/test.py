import happybase

happybase_connection = happybase.Connection(host='192.168.197.24', port=9090)
happybase_connection.open()

# families={
#     'base':dict(),
#     'adress':dict()
#
# }
# happybase_connection.create_table('ytn:python137',families)

#
# connection_table = happybase_connection.table('ytn:python137')
# connection_table.put('001',{'base:name':'ytnnong','base:password':'123456'})



#
#
# table = happybase_connection.table('ytn:python137')
# row = table.row('001')
# print(row)
