#include <iostream>
#include <vector>
#include <cstdlib>

// call: ./a.out NITER R
int main(int argc, char **argv)
{
  const int NITER = std::atoi(argv[1]);
  const double R = std::atof(argv[2]);
  std::vector<double> x(NITER);

  x[0] = 0.12;
  for (int ii = 1; ii < NITER; ++ii) {
    x[ii] = R*x[ii-1]*(1-x[ii-1]);
  }

  for (int ii = 0; ii < NITER; ++ii) {
    std::cout << ii << "  " << x[ii] << "\n";
  }

  return 0;
}
