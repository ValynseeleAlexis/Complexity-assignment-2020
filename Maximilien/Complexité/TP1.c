#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <unistd.h>



void hanoi(int n,int d,int a,int i)
{
    if(n!=0)
    {
        hanoi(n-1,d,i,a);
        hanoi(n-1,i,a,d);
    }
}


int suiteRec(int n)
{
    if(n==0)
        return 1;
    else if(n==1)
        return 1;
    else
        return suiteRec(n-1)+suiteRec(n-2);
}

int suiteIteratif(int n)
{
    int un1=1;
    int un2=1;
    int un;
    for(int i=2;i<n+1;i++)
    {
        un=un1+un2;
        un2=un1;
        un1=un;
    }
    return un;
}


/*void funcHanoi(const char* tab)
{
    clock_t start, finish;
    char file[20]="dataHanoi";
    char str[10];
    
    for (int n=0;n<atoi(tab[1]);n++)
    {
        sprintf(str,"%d",n);
        char path[20];
        strcpy(path,file);
        strcat(path,str);
        strcat(path,".txt");
        FILE *f=fopen(path,"w");
        for (int i=0;i<=25;i++)
        {
            start=clock();
            hanoi(i,1,2,3);
            finish=clock();
            fprintf(f,"%f\n",(double)(finish-start)/CLOCKS_PER_SEC);
        }
        fclose(f);
    }
    system("python .\\tp1.py");
}
*/



/* Helper function that multiplies 2 matrices F and M of size 2*2, and 
  puts the multiplication result back to F[][] */
void multiply(int F[2][2], int M[2][2]); 
  
/* Helper function that calculates F[][] raise to the power n and puts the 
  result in F[][] 
  Note that this function is designed only for fib() and won't work as general 
  power function */
void power(int F[2][2], int n); 
  
int fib(int n) 
{ 
  int F[2][2] = {{1,1},{1,0}}; 
  if (n == 0) 
      return 0; 
  power(F, n-1); 
  
  return F[0][0]; 
} 
  
void multiply(int F[2][2], int M[2][2]) 
{ 
  int x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]; 
  int y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]; 
  int z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]; 
  int w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]; 
  
  F[0][0] = x; 
  F[0][1] = y; 
  F[1][0] = z; 
  F[1][1] = w; 
} 
  
void power(int F[2][2], int n) 
{ 
  int i; 
  int M[2][2] = {{1,1},{1,0}}; 
  
  // n - 1 times multiply the matrix to {{1,0},{0,1}} 
  for (i = 2; i <= n; i++) 
      multiply(F, M); 
} 
  







void cribleDerastotene(int n)
{
    int *tab = (int *)malloc((n+1)*sizeof(int));
    for (int i=0;i<=n;i++)
    {
        tab[i]=0;
    }
    tab[0]=tab[1]=1;
    int i=2;
    while (i<=sqrt(n))
    {
        if(tab[i]==0)
        {
            for(int j=i+1;j<=n;j++)
                if(j%i==0)
                    tab[j]=1;
        }
        i++;
    }
    free(tab);
}



int main(int argc, char const *argv[])
{
    clock_t start, finish;
    FILE *f1=fopen("dataCribleDerastotene.txt","w");
    for(int i=1;i<10000;i++)
    {
        
        float temps;
        start=clock();
        cribleDerastotene(i);/*Traitement*/
        finish=clock();
        temps=(finish-start);

        fprintf(f1,"%f\n",temps/1000000);
    }
    fclose(f1);
    system("python .\\tp1.py");
    return 0;
}







/*int main(int argc, char const *argv[])
{
    clock_t start, finish;
    FILE *f1=fopen("dataFiboMatrix.txt","w");
    for (int i=1;i<=10000;i++)
    {
        start=clock();
        fib(i);
        finish=clock();
        fprintf(f1,"%f\n",(double)(finish-start)/CLOCKS_PER_SEC);
    }
    fclose(f1);
    system("python .\\tp1.py");
    return 0;
}
*/




/*int main(int argc, char const *argv[])
{
    clock_t start, finish;
    FILE *f1=fopen("dataSuiteIte.txt","w");
    FILE *f2=fopen("dataSuiteRec.txt","w");
    for (int i=1;i<=10000;i++)
        {
            start=clock();
            suiteIteratif(i);
            finish=clock();
            fprintf(f1,"%f\n",(double)(finish-start)/CLOCKS_PER_SEC);
            start=clock();
            suiteRec(i);
            finish=clock();
            fprintf(f2,"%f\n",(double)(finish-start)/CLOCKS_PER_SEC);
        }
    fclose(f1);
    fclose(f2);
    system("python .\\tp1.py");
    return 0;
}*/
