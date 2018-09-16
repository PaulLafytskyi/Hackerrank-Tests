# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
#
# Given the number of trailing days  and a client's total daily expenditures for a period of  days, find and print the number of times the client will receive a notification over all  days.
#
# For example,  and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is  and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.
#
# Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the two middle values. (Wikipedia)
#


from bisect import bisect_left, insort_left

n, d = map(int, input().split())
t = list(map(int, input().split()))
noti = 0

lastd = sorted(t[:d])
def med():
    return lastd[d//2] if d % 2 == 1 else ((lastd[d//2] + lastd[d//2-1])/2)

for i in range(d, n):
    if t[i] >= 2*med():
        noti += 1
    del lastd[bisect_left(lastd,t[i-d])]
    insort_left(lastd, t[i])
print(noti)


#
# n,d = input().strip().split(' ')
# n,d = [int(n),int(d)]
# moneys = [int(money) for money in input().strip().split(' ')]
# notification=0
#
# med = moneys[:d]
# def findIdx(st,ed,v):
# 	if(med[st]==v):
# 		return st
# 	if(med[ed]==v):
# 		return ed
# 	if st==ed or st+1==ed:
# 		return ed
#
# 	if med[int((st+ed)/2)]<=v:
# 		return findIdx(int((st+ed)/2),ed,v)
# 	else:
# 		return findIdx(st,int((st+ed)/2),v)
#
# med.sort()
# for i in range(d,n):
# 	if d%2==1:
# 		m = med[int(d/2)]*2
# 	else:
# 		m = med[int(d/2)]+med[int(d/2)-1]
# 	if moneys[i]>=m:
# 		notification+=1
# 	del med[findIdx(0,d-1,moneys[i-d])]
# 	med.insert(findIdx(0,d-2,moneys[i])+1,moneys[i])
# print(notification)
#
#

