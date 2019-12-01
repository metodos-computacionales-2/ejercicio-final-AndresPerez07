#include <iostream>
#include <cmath>
#include <stdlib.h>
#include<fstream>

//Global variables declaring
const double G=9.8;
const double dt=0.01; //Step for th method //M_PI/300.0;
const double eps=0.001;
//theta''+g/l theta + q theta' = F_d sin(Omega t)

class Pendulum
{
public:
  double L; //Lenght
  double q; //Friction coeficient
  double Fd; //External Force
  double Omega; //External force frequency
  double W; //Angular velocity
  double Theta; //Angle
  Pendulum();// Initial values for the class
  ~Pendulum();//Anihilator
};
Pendulum::Pendulum()
{
  L=0.0;
  q=0.0;
  Fd=0.0;
  Omega=0.0;
  W=0.0;
  Theta=0.0;
}
Pendulum::~Pendulum()
{
}

//------------------------------Function declaring----------------------------
void initial_conditions(Pendulum & p, double theta_0, double delta, double FD);
void euler_cromer(Pendulum & p,double dt,double t);

int main(int argc, char** argv)
{
  Pendulum p;
  double t=0.0;//Time
  int N = atoi(argv[1]);//steps of evolution
  double delta = 0.005;
  double theta_0 = 0.2;
  double *FD = new double [4];
  FD[0] = 1.35;
  FD[1] = 1.44;
  FD[2] = 1.465;
  FD[3] = 1.77;

  // intialization
  for (int jj=0; jj<4; jj++){
    t = 0.0;
    initial_conditions(p,theta_0, 0.0, FD[jj]);
    std::ofstream file;
    file.open("data_"+std::to_string(FD[jj])+".dat");
    for (int ii=1; ii<=N; ii++)
      {
        euler_cromer(p,dt,t);
        file << t << "\t" << p.Theta << "\t" << p.W  << std::endl;
        t+=dt;
      }
    file.close();
    t = 0.0;
    initial_conditions(p,theta_0, 0.05, FD[jj]);
    std::ofstream file2;
    file2.open("data_"+std::to_string(FD[jj])+"_delta.dat");
    for (int ii=1; ii<=N; ii++)
      {
        euler_cromer(p,dt,t);
        file2 << t << "\t" << p.Theta << "\t" << p.W  << std::endl;
        t+=dt;
      }
    file2.close();
  }
  double deltaF = 0.01;
  double Fuerza = 1.35;
  double deltaTheta = 0.01;
  int N_bif = 10000;

  std::ofstream file3;
  file3.open("bifurcacion.dat");
  while(Fuerza < 1.5){
    theta_0 = 0.01;
    while(theta_0 < 1.0){
      t = 0.0;
      initial_conditions(p,theta_0, 0.0, Fuerza);
      for (int ii=1; ii<=N_bif; ii++)
        {
          euler_cromer(p,dt,t);
          t+=dt;
        }
        file3 << Fuerza << "\t" << p.Theta << std::endl;
        theta_0 = theta_0 + deltaTheta;
    }

    Fuerza = Fuerza + deltaF;
  }
  file3.close();

  delete []FD;
  return 0;
}


// ------------------- Functions ------------------------------------
void euler_cromer(Pendulum & p,double dt,double t)
{
  // Euler- Cromer
  p.W=p.W+(-(G/p.L)*sin(p.Theta) - p.q*p.W + p.Fd*sin(p.Omega*t))*dt;
  p.Theta=p.Theta + p.W*dt;
  if(p.Theta < - M_PI)
    {
      p.Theta += 2*M_PI;
    }
  else if(p.Theta > M_PI)
    {
      p.Theta += -2*M_PI;
    }
}

void initial_conditions(Pendulum & p, double theta_0, double delta, double FD)
{
  p.q=0.5;
  p.Fd=FD;
  p.Omega=0.666;
  p.L=G;
  p.W=0.0;
  p.Theta=theta_0 + delta;
}
