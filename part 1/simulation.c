#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int moving, startx, starty;
static int pos_x=2,pos_y=2,pos_z=1;
static int angles[]={0.0,-40.0,30.0,0.0,0.0,0.0};

float m=0;
float a=0;
char flag=0;
float time=0.0;
float T1=0;
float T2=0;
float x_y=2.0;
GLfloat angle = 0.0;   /* in degrees */
GLfloat angle2 = 0.0;
GLfloat angle3= 0.0;
GLfloat reset= 0.0;   /* in degrees */


void init(void)
{
   glClearColor(0.0, 0.0, 0.0, 0.0);
   glShadeModel(GL_FLAT);
}


void pyramid(float x_s ,float y_s,float z_s,float x,float y,float z,float x_a,float y_a,float z_a)
{
glPushMatrix();
glColor3f(1,1,1);
glTranslatef(x,y,z);
glRotatef(y_a,0,1,0);
glRotatef(z_a,0,0,1);
glRotatef(x_a,1,0,0);
glScalef(x_s,y_s,z_s);
glBegin( GL_TRIANGLES );


glVertex3f( 0.0f, 1.f, 0.0f );
glVertex3f( -1.0f, -1.0f, 1.0f );
glVertex3f( 1.0f, -1.0f, 1.0f);

glVertex3f( 0.0f, 1.0f, 0.0f);
glVertex3f( -1.0f, -1.0f, 1.0f);
glVertex3f( 0.0f, -1.0f, -1.0f);


glVertex3f( 0.0f, 1.0f, 0.0f);
glVertex3f( 0.0f, -1.0f, -1.0f);
glVertex3f( 1.0f, -1.0f, 1.0f);

glVertex3f( -1.0f, -1.0f, 1.0f);
glVertex3f( 0.0f, -1.0f, -1.0f);
glVertex3f( 1.0f, -1.0f, 1.0f);


glEnd();
glPopMatrix();

}





void display(void)
{

   glClear(GL_COLOR_BUFFER_BIT);
   glPushMatrix();


   glRotatef(angle2, 1.0, 0.0, 0.0);
   glRotatef(angle, 0.0, 1.0, 0.0);

 
   glTranslatef(pos_x,pos_y,pos_z);
   glRotatef(angles[3], 0.0, 0.0, 1.0);
   glRotatef(angles[2], 1.0, 0.0, 0.0);
   glRotatef(angles[1], 0.0, 1.0, 0.0);


  pyramid(.1,.1,.1,2.5,0,0,0,0,-90);
  pyramid(.1,.1,.1,-2.5,0,0,0,0,90);
  pyramid(.1,.1,.1,0,2.5,0,0,0,0);
  pyramid(.1,.1,.1,0,-2.5,0,0,0,180);
  pyramid(.1,.1,.1,0,0,2.5,90,0,0);
  pyramid(.1,.1,.1,0,0,-2.5,-90,0,00);
  
  // glPushMatrix();
  // glColor3f(0,0,1);
  // glRotatef(90.0,1,0,0);
  // glutWireSphere(2,20,20);
  // glPopMatrix();  
  


   glBegin(GL_LINE_LOOP);
 
   for (int i=0,j=0; i <=360*5; i++,j++)
   {
      float degInRad = 3.141592/180;
      glColor3f(.5,.7,0);

        a=2*(1-exp(-i*10/T1));
        a=acos(a/2.0)*(180.0/3.141592);
      // glVertex3f(cos(degInRad)*2,i,sin(degInRad)*2);
      glVertex3f(2*sin(a *degInRad)*cos(((5*j)%360)*degInRad),2*cos(a*degInRad) ,2*sin(a*degInRad)*sin(((5*j)%360)*degInRad) );
   }
 
   glEnd();


  glBegin(GL_LINES);
  glPushMatrix();
  glColor3f(1,1,1);
  glVertex3d(0,0,0);
  glVertex3d(2.5,0,0);
  glPopMatrix();
  glEnd();
  glBegin(GL_LINES);
  glPushMatrix();
  glColor3f(1,1,1);
  glVertex3d(0,0,0);
  glVertex3d(-2.5,0,0);
  glPopMatrix();
  glEnd();


  glBegin(GL_LINES);
  glPushMatrix();
  glVertex3d(0,0,0);
  glVertex3d(0,2.5,0);
  glPopMatrix();
  glEnd();
  glBegin(GL_LINES);
  glPushMatrix();
  glVertex3d(0,0,0);
  glVertex3d(0,-2.5,0);
  glPopMatrix();
  glEnd();

  glBegin(GL_LINES);
  glPushMatrix();
  glVertex3d(0,0,0);
  glVertex3d(0,0,2.5);
  glPopMatrix();
  glEnd();
    glBegin(GL_LINES);
  glPushMatrix();
  glVertex3d(0,0,0);
  glVertex3d(0,0,-2.5);
  glPopMatrix();
  glEnd();



  glPushMatrix();
  glRotatef((GLfloat)angles[0],0.0,1.0,0.0);
  glPushMatrix();
  glTranslatef(x_y,0,0);
  glColor3f(1,1,.2);
  glutWireSphere(.1,20,20);
  glPopMatrix();  


  glBegin(GL_LINES);
  glPushMatrix();
  glColor3f(1,1,.2);
  glVertex3d(0,0,0);
  glVertex3d(x_y,0,0);
  glPopMatrix();
  glEnd();



  glRotatef((GLfloat)angle3,0.0,0.0,1.0);
  

  glPushMatrix();
  glTranslatef(0,2,0);
  glColor3f(1,0,0);
  glutWireSphere(.1,20,20);
  glPopMatrix();  


  glBegin(GL_LINES);
  glPushMatrix();
  glColor3f(1,0,0);
  glVertex3d(0,0,0);
  glVertex3d(0,2,0);
  glPopMatrix();
  glEnd();
glPopMatrix();

glPushMatrix();
  glRotatef((GLfloat)angles[4],0.0,1.0,0.0);
  glRotatef((GLfloat)angle3,0.0,0.0,1.0);
  

  glPushMatrix();
  glTranslatef(0,2,0);
  glColor3f(0,1,0);
  glutWireSphere(.1,20,20);
  glPopMatrix();  


  glBegin(GL_LINES);
  glPushMatrix();
  glColor3f(0,1,0);
  glVertex3d(0,0,0);
  glVertex3d(0,2,0);
  glPopMatrix();
  glEnd();
glPopMatrix();

glPushMatrix();
  glRotatef((GLfloat)angles[5],0.0,1.0,0.0);
  glRotatef((GLfloat)angle3,0.0,0.0,1.0);
  

  glPushMatrix();
  glTranslatef(0,2,0);
  glColor3f(0,0,1);
  glutWireSphere(.1,20,20);
  glPopMatrix();  


  glBegin(GL_LINES);
  glPushMatrix();
  glColor3f(0,0,1);
  glVertex3d(0,0,0);
  glVertex3d(0,2,0);
  glPopMatrix();
  glEnd();
glPopMatrix();


 




  
  



   
   glPopMatrix();
   glutSwapBuffers();
}

void reshape(int w, int h)
{
   glViewport(0, 0, (GLsizei)w, (GLsizei)h);
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   gluPerspective(90.0, (GLfloat)w / (GLfloat)h, 0.0, 75.0);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   glTranslatef(-2.0, -2.0, -5.0);
}


void decay(float x)
{

if (flag==0){
  if (angle3 > 3  ){
  m=2*(1-exp(-x/T1));
  angle3=acos(m/2.0)*(180.0/3.141592);
  
  x_y=2*exp(-x/T2);
 }
}
else
{
  time=-T1 * log(1-(cos(reset*(3.141592/180.0 ) )));
 if (angle3 < reset-5){
  angle3+=5;
  x_y=2.0;
  angles[0]=180;


  
 }
 else
 {
   flag=0;
 }

 
}


}

void timer(int x)
{
    

    angles[0]-=5;
    angles[0]%=360;
    angles[4]-=7;
    angles[4]%=360;
    angles[5]-=3;
    angles[5]%=360;
    time+=10.0;
    decay(time);

    glutPostRedisplay();    
    glutTimerFunc(10, timer,0);
    
}






void keyboard(unsigned char key, int x, int y)
{
   switch (key)
   {
   case 'a':
      flag=1;
      glutPostRedisplay();
    break;
       case 'q':
      angles[1]+=5;
      angles[1]%=360;
      glutPostRedisplay();
    break;
       case 'w':
      angles[2]+=5;
      angles[2]%=360;
      
      glutPostRedisplay();
    break;
       case 'e':
      angles[3]+=5;
      angles[3]%=360;
      glutPostRedisplay();
    break;


      case 'Q':
      angles[1]-=5;
      angles[1]%=360;
      glutPostRedisplay();
    break;
       case 'W':
      angles[2]-=5;
      angles[2]%=360;
      
      glutPostRedisplay();
    break;
       case 'E':
      angles[3]-=5;
      angles[3]%=360;
      glutPostRedisplay();
    break;

    case '5':
      pos_z-=1;
      glutPostRedisplay();
    break;

       case '4':
      pos_x-=1;
      glutPostRedisplay();
    break;

      case '6':
      pos_x+=1;
      glutPostRedisplay();
    break;

     case '8':
      pos_y+=1;
      glutPostRedisplay();
    break;

     case '2':
      pos_y-=1;
      glutPostRedisplay();
    break; 

     case '0':
      pos_z+=1;
      glutPostRedisplay();
    break;

            
    
    break; 
     case 'z':
    angles[0]=0;
    angles[1]=-40;
    angles[2]=30;
    pos_x=2;
    pos_y=2;
    pos_z=1;
    glutPostRedisplay();
    break;

   case 27:
      exit(0);
      break;
   default:
      break;
   }
}

static void mouse(int button, int state, int x, int y)
{
  if (button == GLUT_LEFT_BUTTON) {
    if (state == GLUT_DOWN) {
      moving = 1;
      startx = x;
      starty = y;
    }
    if (state == GLUT_UP) {
      moving = 0;
    }
  }
}


static void motion(int x, int y)
{
  if (moving) {
    angle = angle + (x - startx);
    angle2 = angle2 + (y - starty);
    startx = x;
    starty = y;
    glutPostRedisplay();
  }
}



int main(int argc, char **argv)
{  
  
   T1=atoi(argv[2]);
   T2=atoi(argv[3]); 
   angle3= atoi(argv[1]);
   
   time=-T1 * log(1-(cos(atoi(argv[1])*(3.141592/180.0  ))));
   reset=angle3; 

  

   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
   glutInitWindowSize(750, 500);
   glutInitWindowPosition(100, 100);
  glutTimerFunc(0, timer,0);
   glutCreateWindow(argv[0]);
   init();
   glutMouseFunc(mouse);
   glutMotionFunc(motion);
   glutDisplayFunc(display);
   glutReshapeFunc(reshape);
   glutKeyboardFunc(keyboard);
   glutMainLoop();
   return 0;
}