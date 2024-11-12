import rosbag

bag = rosbag.Bag('Rose115ptClds.bag')
f = open('FLS_Messages.txt', 'x')

print("Topics:", bag.get_type_and_topic_info()[1].keys())

for topic, msg, t in bag.read_messages(topics=['/rose']):
    print(f"Timestamp: {t.to_sec()}")
    print("Message:", msg)
    f.write("Time: " + str(t.to_sec()) + "\n")
    f.write(str(msg) + '\n')

bag.close()
f.close()