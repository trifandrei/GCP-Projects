def summary_dict(string_data):
        list1=string_data.split('\n')
        return [{"sender":data[data.index("sender:")+ len("sender:") + 1: data.index("message:")],"reciver":data[data.index("receiver:") + len("receiver:") + 1:-1],"message":data[data.index(" “") + len("“") + 1: data.index("”")]} for data in list1[:-1] ]
  


string_data="id_00 sender: Maria message: “hello Gina, How are you?” receiver: Gina \n id_01 sender: Dorin message: “Good Morning” receiver: Nicu \n"
print(summary_dict(string_data))