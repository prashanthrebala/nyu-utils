
##### INPUT VALUES #####
alpha = 0.125
beta = 0.25

rtt_s_0 = 200
rtt_d_0 = 87.2

G = 4

rtt_m = [287.073, 201.508, 355.714]
##### END OF INPUT VALUES #####

rtt_s = [rtt_s_0, 0, 0, 0]
rtt_d = [rtt_d_0, 0, 0, 0]

rto = 0

for i in range(1, 4):
    rtt_s[i] = (1 - alpha) * rtt_s[i - 1] + alpha * rtt_m[i - 1]
    rtt_d[i] = (1 - beta) * rtt_d[i - 1] + beta * abs(rtt_m[i - 1] - rtt_s[i - 1]);


rto = max(200, rtt_s[-1] + G * rtt_d[-1])

print("RTTs", rtt_s[1: ])
print("RTTd", rtt_d[1: ])
print("RTO", rto)
print("RTO2", rto * 2)