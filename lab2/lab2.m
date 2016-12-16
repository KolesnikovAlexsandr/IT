function tzel=svetofor1(vrz,y1,y2)
vrz= 30;
cycle=60;
r=newfis('svetofor');
 
r=addvar(r,'input','врем€ зеленого света',[10 50]);
r=addmf(r,'input',1,'малое','trapmf',[10 10 20 25]);
r=addmf(r,'input',1,'среднее','trapmf',[20 25 35 40]);
r=addmf(r,'input',1,'большое','trapmf',[35 40 50 50]);

r=addvar(r,'input','улица —евер-ёг',[0 90]);
r=addmf(r,'input',2,'очень малое','trapmf',[0 0 12 18]);
r=addmf(r,'input',2,'малое','trapmf',[15 21 31 37]);
r=addmf(r,'input',2,'среднее','trapmf',[34 40 50 56]);
r=addmf(r,'input',2,'большое','trapmf',[53 59 69 75]);
r=addmf(r,'input',2,'очень большое','trapmf',[72 78 90 90]);

r=addvar(r,'input','улица «апад-¬осток',[0 90]);
r=addmf(r,'input',3,'очень малое','trapmf',[0 0 12 18]);
r=addmf(r,'input',3,'малое','trapmf',[15 21 31 37]);
r=addmf(r,'input',3,'среднее','trapmf',[34 40 50 56]);
r=addmf(r,'input',3,'большое','trapmf',[53 59 69 75]);
r=addmf(r,'input',3,'очень большое','trapmf',[72 78 90 90]);

r=addvar(r,'output','врем€ зел.света на улице —ё',[-20 20]); 
r=addmf(r,'output',1,'увеличить','gaussmf',[7 20]);
r=addmf(r,'output',1,'не измен€ть','gaussmf',[7 0]);
r=addmf(r,'output',1,'уменьшить','gaussmf',[7 -20]);
list=[
1 1 1 1 1 1
1 1 2 1 1 1
1 1 3 1 1 1
1 1 4 2 1 1
1 1 5 2 1 1
1 2 1 1 1 1
1 2 2 1 1 1
1 2 3 1 1 1
1 2 4 2 1 1
1 2 5 2 1 1
1 3 1 1 1 1
1 3 2 1 1 1
1 3 3 1 1 1
1 3 4 1 1 1
1 3 5 2 1 1
1 4 1 1 1 1
1 4 2 1 1 1
1 4 3 1 1 1
1 4 4 1 1 1
1 4 5 1 1 1
1 5 1 1 1 1
1 5 2 1 1 1
1 5 3 1 1 1
1 5 4 1 1 1
1 5 5 1 1 1
2 1 1 2 1 1
2 1 2 2 1 1
2 1 3 3 1 1
2 1 4 3 1 1
2 1 5 3 1 1
2 2 1 1 1 1
2 2 2 2 1 1
2 2 3 3 1 1
2 2 4 3 1 1
2 2 5 3 1 1
2 3 1 1 1 1
2 3 2 1 1 1
2 3 3 2 1 1
2 3 4 3 1 1
2 3 5 3 1 1
2 4 1 1 1 1
2 4 2 1 1 1
2 4 3 1 1 1
2 4 4 2 1 1
2 4 5 3 1 1
2 5 1 1 1 1
2 5 2 1 1 1
2 5 3 1 1 1
2 5 4 1 1 1
2 5 5 2 1 1
3 1 1 3 1 1
3 1 2 3 1 1
3 1 3 3 1 1
3 1 4 3 1 1
3 1 5 3 1 1
3 2 1 3 1 1
3 2 2 3 1 1
3 2 3 3 1 1
3 2 4 3 1 1
3 2 5 3 1 1
3 3 1 2 1 1
3 3 2 3 1 1
3 3 3 3 1 1
3 3 4 3 1 1
3 3 5 3 1 1
3 4 1 2 1 1
3 4 2 2 1 1
3 4 3 2 1 1
3 4 4 3 1 1
3 4 5 3 1 1
3 5 1 2 1 1
3 5 2 2 1 1
3 5 3 2 1 1
3 5 4 3 1 1
3 5 5 3 1 1];
r=addrule(r,list);
for i= 1:100
  y1= randi([0 90],1);
  y2= randi([0 90],1);
  if(i>1)
      y1= y1-vrz;
      y1= round(y1);
      if(y1<0)
          y1=0;
      end
      y2= y2-(cycle-vrz);
      y2= round(y2);
      if(y2<0)
          y2=0;
      end
  end
autoarray(i)= y1+y2;      
tzel=evalfis([vrz, y1, y2],r);
vrz=vrz+tzel;
end
average=0;
for p= 1:100
    average= average+autoarray(p);
end
average=average/100;
disp('average= ');
disp(average);