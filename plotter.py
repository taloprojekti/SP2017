def graph(data,running_times):
    #creates a plot of price of electricity and heating times 
    import matplotlib.pyplot as plt
    import numpy as np
    y_max = max(running_times)
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],data,"b",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],running_times,"r")
    plt.axis([1,24,0,y_max+10])
    plt.title("Price of electricity",fontsize="large",fontweight="bold")
    plt.text(1.2, y_max+7.9, "Price of the day", fontsize="large",ha = "left",color="blue",fontweight="bold")
    plt.text(1.2,y_max+5.9,"Heating on/off", fontsize="large",ha="left",color="red",fontweight="bold")
    plt.ylabel("EUR/MWh")
    plt.xlabel("Hours")
    plt.show()


def main():
    from jsonhandler import importJSON
    data = importJSON("data/graph.json")
    print(data)
    y_axis = []
    i = 0
    while i < 24:
        y_axis.append(data[str(i)])
        i += 1
    y_max = max(y_axis)
    print(y_max)
    running_times = importJSON("data/graph2.json")
    for n, value in enumerate(running_times):
        if value == 1:
            running_times[n] = int(y_max)
    print(running_times)
    graph(y_axis,running_times)

main()

