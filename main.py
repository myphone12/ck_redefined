# from reck import Ck
# # from UI import Ck_UI

# a = Ck()
# for i in range(1,100):
#     print(a.ck(i),end="")
#     print(a.dt, end=" | ")
#     # print(f'a[{i-1}]:{a[i-1]}')
#     # print(a)

import UI
a = UI.ItemDataSettings_UI()


a.PrepareUILoading()
a.Mainloop()