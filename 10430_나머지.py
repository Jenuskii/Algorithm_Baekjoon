'''
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

출력
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

예제 입력 1 
5 8 4
예제 출력 1 
1
1
0
0
'''
a, b, c = map(int, input().split())
print((a+b) % c)
print(((a%c)+(b%c)) % c)
print((a*b) % c)
print(((a%c)*(b%c)) % c)

#다른 풀이, 대입 표현식 구문(바다코끼리 연산자 :=) 코드는 더 짧지만 속도는 불리함
a,b,c=map(int,input().split())
print(x:=(a+b)%c,x,y:=a*b%c,y,sep='\n')