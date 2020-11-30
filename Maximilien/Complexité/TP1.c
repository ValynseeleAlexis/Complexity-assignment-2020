#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>




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

int main(int argc, char const *argv[])
{
    clock_t start, finish;
    FILE *f1=fopen("dataSuiteIte.txt","w");
    FILE *f2=fopen("dataSuiteRec.txt","w");
    for (int i=1;i<=100000;i++)
        {
            start=clock();
            suiteIteratif(i);
            finish=clock();
            fprintf(f1,"%f\n",(double)(finish-start)/CLOCKS_PER_SEC);
            /*start=clock();
            suiteRec(i);
            finish=clock();
            fprintf(f2,"%f\n",(double)(finish-start)/CLOCKS_PER_SEC);*/
        }
    fclose(f1);
    fclose(f2);
    system("python .\\tp1.py");
    return 0;
}
