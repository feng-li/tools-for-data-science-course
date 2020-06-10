from matplotlib import pyplot as plt
days = [3, 4, 5, 6, 7, 8, 9]
bitprice = [8812.95, 8845.67, 8843.9, 9272.37, 9517.01, 9939.29, 9817.29]
fig = plt.figure()
plt.plot(days, bitprice, color='green', marker='o', linestyle='solid')
# add a title
plt.title("The Price of Bitcoin from May 3rd to 9th")
plt.show()
