//author : keyur rakholiya
//algorithm: wavefront
//email: keyurrakholiya302@gmail.com


#include <stdio.h>
//#include <conio.h>
#define row 20
#define col 20
#define loop_no 400									 //(it should be 20*20 = 400 idealy)

/*

int map[6][6] =   {{1,1,1,1,1,1},				//keep one row and one column extra
		   {1,'R',1,1,0,1},
		   {1,1,1,1,0,1},
		   {1,0,1,1,0,1},
		   {1,2,1,1,0,1},
		   {1,1,1,1,1,1}};
*/

int map[20][20] = {{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},				//keep one row and one column extra
		   {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
		   {1,'R',1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
		   {1,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1},
		   {1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1},
		   {1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1},
		   {1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1},				//keep one row and one column extra
		   {1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1},
		   {1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1},
		   {1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1},
		   {1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
		   {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}}; 

int i,j,k,I,J,l,count;
int temp1,temp2,temp3,temp4,sum1,sum2,sum3,sum4,temp=2;
int r1,r2,r3,r4,c1,c2,c3,c4,flag = 1;
int path[4][100];
int row_desti,col_desti,path_num,new_path[50],length;
int r_row,r_col,cordinate;
int pos = 0;
int ind1=0,ind2=0,ind3=0,ind4=0;
int path_flag  = 1;
int go = 1;
void flush()
{
i=0;j=0;k=0,I=0;J=0;l=0;
temp1=0;temp2=0;temp3=0;temp4=0;sum1=0;sum2=0;sum3=0;sum4=0;temp=2;
r1=0;r2=0;r3=0;r4=0;c1=0;c2=0;c3=0;c4=0;flag = 1;
length=0;
cordinate=0;
}

void path_find(void)
{	flush();
	
	for (k = 0;k<4;k++)
		{ printf("\n");
		for(l=0; l<100; l++)
			{
				path[k][l] = 0;
				ind1 = 0;
				ind2 = 0;
				ind3 = 0;
				ind4 = 0;
			}
		}


		
	

			

	
	i=0;
	j=0;
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			
			if(map[i][j] == 2) //find goal 'G'
				{
					printf("i = %d j = %d ",i,j);
					map[i][j] = 2;
					row_desti = i;
					col_desti = j;
				}
		}
	}

	
	printf("\n");

	
	while(temp < loop_no)
	{
		//printf("\n value of temp = %d" ,temp);
		for(i=0;i<row;i++)
		{
			for(j=0;j<col;j++)
			{
				if(map[i][j] == temp)
				{
				
					k = temp;

					//printf("\n value of k = %d" ,k);
					if((map[i][j+1] != 1) && (map[i][j+1] != 'R') && (map[i][j+1] < 2)) map[i][j+1] = temp + 1;
					if((map[i][j-1] != 1) && (map[i][j-1] != 'R') && (map[i][j-1] < 2)) map[i][j-1] = temp + 1;
					if((map[i+1][j] != 1) && (map[i+1][j] != 'R') && (map[i+1][j] < 2)) map[i+1][j] = temp + 1; 						if((map[i-1][j] != 1) && (map[i-1][j] != 'R') && (map[i-1][j] < 2)) map[i-1][j] = temp + 1;
			
					/*if(map[i][j+1] ==0) map[i][j+1] = temp + 1;
					if(map[i][j-1] ==0) map[i][j-1] = temp + 1;
					if(map[i+1][j] ==0) map[i+1][j] = temp + 1; 						
					if(map[i-1][j] ==0) map[i-1][j] = temp + 1;*/
				}
			
			}
		}

		/*for(i=0;i<row;i++)
		{
			printf("\n");
			for(j=0;j<col;j++)
			{
				printf("%d \t",map[i][j]);
			}
		}*/
		temp = temp + 1;
	

	}
	
	
	//finding the path
		
		//robot current location
		for(I=0;I<row;I++)
		{
			for(J=0;J<col;J++)
			{
				if(map[I][J] == 'R')
					{
						printf("keyur i = %d j = %d ",I,J);
						i= I;
						r_row = I;
						j = J;
						r_col = J;
					}
			}
		}
		
		
		temp1 = map[i][j-1]; 
		r1 = i;
		c1 = j-1;	 //column decrement
		
		path[0][ind1] = r1;
		path[0][ind1+1] = c1;
		sum1 = temp1;
		//printf("temp1 =%d",sum1);
		
		
		temp2 = map[i][j+1]; //columne increment
		r2 = i;
		c2 = j+1;
		path[1][ind2] = r2;
		path[1][ind2+1] = c2;
		sum2 = temp2;
		//printf("temp2= %d",sum2);

		temp3 = map[i+1][j]; //row increment
		r3 = i+1;
		c3 = j;
		path[2][ind3] = r3;
		path[2][ind3+1] = c3;
		sum3 = temp3;
		//printf("temp3= %d",sum3);

		temp4 = map[i-1][j]; //row decrement
		r4 = i-1;
		c4 = j;
		path[3][ind4] = r4;
		path[3][ind4+1] = c4;	
		sum4 = temp4;
		//printf("temp4=%d",sum4);	
		
		while(flag == 1)
		{
				//printf("maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaking path");
		if(temp1 > 2)
			{//	printf("\tnewtemp1 = %d",temp1);
				if(map[r1][c1-1] == map[r1][c1] - 1)
				{
					sum1 = sum1 + map[r1][c1-1];
					temp1 = map[r1][c1-1];
					
					ind1= ind1 + 2;
					path[0][ind1]= r1;
					path[0][ind1+1] = c1-1;
					
					if(map[r1][c1-1] == 2) {flag = 0;}
					c1 = c1 - 1;
					
				}
				
				else if(map[r1][c1+1] == map[r1][c1] - 1)
				{
					sum1 = sum1 + map[r1][c1+1];
					temp1 = map[r1][c1+1];
					
					ind1= ind1 + 2;
					path[0][ind1]= r1;
					path[0][ind1+1] = c1+1;
					
					if(map[r1][c1+1] == 2) {flag = 0;}
					c1 = c1 + 1;
					
				}

				else if(map[r1+1][c1] == map[r1][c1] - 1)
				{
					
					sum1 = sum1 + map[r1+1][c1];
					temp1 = map[r1+1][c1];

					ind1 = ind1 + 2;
					path[0][ind1]= r1+1;
					path[0][ind1+1] = c1;

					if(map[r1+1][c1] == 2) {flag = 0;}
					r1 = r1 +1;
				}
				else if(map[r1-1][c1] == map[r1][c1] -1 )
				{
					sum1 = sum1 + map[r1-1][c1];
					temp1 = map[r1-1][c1];

					ind1 = ind1 + 2;
					path[0][ind1]= r1-1;
					path[0][ind1+1] = c1;					

					if(map[r1-1][c1] == 2) {flag = 0;}
					r1 = r1 -1;
				}
			}
			

		if(temp2 > 2 )
			{	//printf("\tnewtemp2 = %d",temp2);
				if(map[r2][c2+1] == map[r2][c2] - 1)
				{
					sum2 = sum2 + map[r2][c2+1];
					temp2 = map[r2][c2+1];

					ind2 = ind2 + 2;
					path[1][ind2]= r2;
					path[1][ind2+1] = c2+1;

					if(map[r2][c2+1] == 2) {flag = 0;}
					c2 = c2 + 1;

				
				}
				else if(map[r2][c2-1] == map[r2][c2] - 1)
				{
					sum2 = sum2 + map[r2][c2-1];
					temp2 = map[r2][c2-1];

					ind2 = ind2 + 2;
					path[1][ind2]= r2;
					path[1][ind2+1] = c2-1;

					if(map[r2][c2-1] == 2) {flag = 0;}
					c2 = c2 - 1;

				
				}
				else if(map[r2+1][c2] == map[r2][c2] - 1)
				{
					sum2 = sum2 + map[r2+1][c2];
					temp2 = map[r2+1][c2];

					ind2 = ind2 + 2;
					path[1][ind2]= r2 +1;
					path[1][ind2+1] = c2;

					if(map[r2+1][c2] == 2) {flag = 0;}		
					r2 = r2 + 1;
				}
				else if(map[r2-1][c2] == map[r2][c2] -1 )
				{
					sum2 = sum2 + map[r2-1][c2];
					temp2 = map[r2-1][c2];

					ind2 = ind2 + 2;
					path[1][ind2]= r2-1;
					path[1][ind2+1] = c2;

					if(map[r2-1][c2] == 2) {flag = 0;}
					r2 = r2 - 1;
				}
			}
		
	
		if(temp3 > 2 )	//row increment
			{	//printf("\tnewtemp3 = %d",temp3);
				if(map[r3][c3+1] == map[r3][c3] - 1)
				{
					sum3 = sum3 + map[r3][c3+1];
					temp3 = map[r3][c3+1];

					ind3 = ind3 + 2;
					path[2][ind3]= r3;
					path[2][ind3+1] = c3+1;

					if(map[r3][c3+1] == 2) {flag = 0;}
					
					c3 = c3 + 1;
				
				}
				else if(map[r3+1][c3] == map[r3][c3] - 1)
				{
					
					sum3 = sum3 + map[r3+1][c3];
					temp3 = map[r3+1][c3];

					ind3 = ind3 + 2;
					path[2][ind3]= r3+1;
					path[2][ind3+1] = c3;
					
					if(map[r3+1][c3] == 2) {flag = 0;}
					r3 = r3 + 1;
				}
				else if(map[r3-1][c3] == map[r3][c3] - 1)
				{
					
					sum3 = sum3 + map[r3-1][c3];
					temp3 = map[r3-1][c3];

					ind3 = ind3 + 2;
					path[2][ind3]= r3-1;
					path[2][ind3+1] = c3;
					
					if(map[r3-1][c3] == 2) {flag = 0;}
					r3 = r3 - 1;
				}
				else if(map[r3][c3-1] == map[r3][c3] -1 )
				{
					sum3 = sum3 + map[r3][c3-1];
					temp3 = map[r3][c3-1];

					ind3 = ind3 + 2;
					path[2][ind3]= r3;
					path[2][ind3+1] = c3-1;
			
					if(map[r3][c3-1] == 2) {flag = 0;}
					c3 = c3 -1;
				}
				
			}	
		
			
		if(temp4 > 2 )	//row decrement
			{	//printf("\tnewtemp4 = %d",temp4);
				if(map[r4][c4+1] == map[r4][c4] - 1)
				{
					sum4 = sum4 + map[r4][c4+1];
					temp4 = map[r4][c4+1];

					ind4 = ind4 + 2;
					path[3][ind4]= r4;
					path[3][ind4+1] = c4+1;

					if(map[r4][c4+1] == 2) {flag = 0;}
					c4 = c4 + 1;

				
				}
				else if(map[r4-1][c4] == map[r4][c4] - 1)
				{
					
					sum4 = sum4 + map[r4-1][c4];
					temp4 = map[r4-1][c4];

					ind4 = ind4 + 2;
					path[3][ind4]= r4-1;
					path[3][ind4+1] = c4;

					if(map[r4-1][c4] == 2) {flag = 0;}
					r4 = r4 - 1;
				}
				else if(map[r4+1][c4] == map[r4][c4] - 1)
				{
					
					sum4 = sum4 + map[r4+1][c4];
					temp4 = map[r4+1][c4];

					ind4 = ind4 + 2;
					path[3][ind4]= r4+1;
					path[3][ind4+1] = c4;

					if(map[r4+1][c4] == 2) {flag = 0;}
					r4 = r4 + 1;
				}
				else if(map[r4][c4-1] == map[r4][c4] -1 )
				{
					sum4= sum4 + map[r4][c4-1];
					temp4 = map[r4][c4-1];

					ind4 = ind4 + 2;
					path[3][ind4]= r4;
					path[3][ind4+1] = c4-1;
					
					if(map[r4][c4-1] == 2){flag = 0;}
					c4 = c4 - 1;

				}
			}
		
		
		}
	
	

	for(i=0;i<row;i++)
	{
	printf("\n");
		for(j=0;j<col;j++)
		{
			printf("%d ",map[i][j]);
		}
			

	}

	printf("\n all path");
	for (k = 0;k<4;k++)
		{ printf("\n");
		for(l=0; l<99; l++)
			{
				printf("%d",path[k][l]);
			}
		}

	printf("\n finding final path");
		

					
	for(k=0;k<4;k++)
	{
		for(l=0;l<99;)
		{
			if((path[k][l] == row_desti) && (path[k][l+1] == col_desti))
			{
				printf("final path number is %d ",k);
				path_num = k;
				
			}
			l = l+ 2;
		}
	}

	
	
	//printf("sum1 = %d, \t sum2= %d \t ,sum3 = %d \t,sum4 = %d \t",sum1,sum2,sum3,sum4);
	printf("\n last position \t %d",pos);
	
}



int main()
{
	
	path_find();
	
	while(go)

	{	
		
		
		
		count++;
		/*printf ("hello path is %d \n",path_num);
		printf("path[path_num][cordinate] = %d \n",path[path_num][cordinate]);	
		printf("row_desti = %d \n",row_desti);
		printf("path[path_num][cordinate+1] = %d \n",path[path_num][cordinate+1]);	
		printf("col_desti = %d \n",col_desti);
	
		printf("r_row = %d \n",r_row);
		printf("r_col = %d \n",r_col);
		
		printf("helllo rajal \t %d",pos);*/
		if((path[path_num][cordinate]) == r_row + 1)
		{
			//no need to change head position
			if(pos == 0)
			{
				printf("forward \n");
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				pos = 0;
				path_find();
			}
			else if(pos == 90)
			{
				printf("right forward \n");
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				pos = 0;
				path_find();
				
			}	
			else if(pos == 270)
			{
				printf("left forward \n");
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				
				pos = 0;
				path_find();
			}
			else if(pos == 180)
			{
				printf("180 forward \n");
				map[r_row][r_col] = 1;
				map[r_row + 1][r_col] = 'R';
				pos = 0;
				path_find();
			}	
			
	
		}

		else if((path[path_num][cordinate]) == r_row - 1)
		{
			//change head 180 upside
			if(pos == 0)
			{
				printf("180 forward \n");
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
				pos = 180;
				path_find();
			}
			else if(pos == 90)
			{
				printf("left forward \n");
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
				pos = 180;
				path_find();
			}
			else if(pos == 270)
			{
				printf("right forward \n");
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
				pos = 180;
				path_find();
				
			}
			else if(pos == 180)
			{
				printf("forward \n");
				map[r_row][r_col] = 1;
				map[r_row - 1][r_col] = 'R';
			
				pos = 180;
				path_find();
			}
		}

		else if(path[path_num][cordinate+1] ==  r_col + 1) 
		{	
			//left
			
			
			

			if(pos == 0)
			{
				printf("left forward\n");
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();
				
			}
			else if(pos == 90)
			{
				printf("forward \n");
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();
			}
			
			else if(pos == 180)
			{
				printf("right forward\n");
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();	
			}
			else if(pos == 270)
			{
				printf("180 forward\n");
				map[r_row ][r_col + 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 90;
				path_find();
			}	
			
		}

		else if(path[path_num][cordinate+1] ==  r_col - 1)
		{	
			
						
			if(pos == 0)
			{
				printf("right forward\n");
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();
				
			}
			else if(pos == 270 )
			{
				printf("forward\n");
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();
			}
			
			else if(pos == 180)
			{
				printf("left forward\n");
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();	
			}
			else if(pos == 90)
			{
				printf("180 forward\n");
				map[r_row ][r_col - 1] = 'R';
				map[r_row][r_col] = 1;
				pos = 270;
				path_find();
			}
			
				
		}
	if((path[path_num][cordinate+2]== row_desti) && (path[path_num][cordinate+3] == col_desti)) 
		{
			//col incre
			if(((r_col + 1) == path[path_num][cordinate+1] )&&( pos == 0))
				{
					printf("\t left 2time forward");
				}
			else if(((r_col + 1) == path[path_num][cordinate+1] )&&( pos == 180))
				{
					printf("\tright 2time forward");
				}
			else if(((r_col + 1) == path[path_num][cordinate+1] )&&( pos == 90))
				{
					printf("\t2 time forward");
				}
			
			//col decre
			else if(((r_col - 1) == path[path_num][cordinate+1] )&&( pos == 0))
				{
					printf("\tright 2 time forward");
				}
			else if(((r_col - 1) == path[path_num][cordinate+1] )&&( pos == 180))
				{
					printf("\tleft 2 time forward");
				}
			else if(((r_col - 1) == path[path_num][cordinate+1] )&&( pos == 270))
				{
					printf("\t2 time forward");
				}
			//row incre
			else if(((r_row + 1) == path[path_num][cordinate] )&&( pos == 270))
				{
					printf("\tleft 2 time forward");
				}
			else if(((r_row + 1) == path[path_num][cordinate] )&&( pos == 90))
				{
					printf("\tright 2 time forward");
				}
			else if(((r_row + 1) == path[path_num][cordinate] )&&( pos == 0))
				{
					printf("\t2 time forward");
				}
			//row decre
			else if(((r_row - 1) == path[path_num][cordinate] )&&( pos == 90))
				{
					printf("\tleft 2 time forward");
				}
			else if(((r_row - 1) == path[path_num][cordinate] )&&( pos ==270))
				{
					printf("\tright 2 time forward");
				}
			else if(((r_row - 1) == path[path_num][cordinate] )&&( pos == 180))
				{
					printf("\t2 time forward");
				}
			 go = 0; 
			printf("done"); 
		}
	printf("coooooooont %d",count);
	
	}


		
}


