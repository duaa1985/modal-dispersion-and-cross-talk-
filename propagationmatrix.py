import fiber
import utils
import numpy
import scipy
import pickle
sigma_theta = .36
EXTENTS = 30e-6
STEP = .05e-6
x=numpy.arange(-EXTENTS, EXTENTS, STEP)
y=numpy.arange(-EXTENTS, EXTENTS, STEP)
[XX, YY] = numpy.meshgrid(x,y)
theta_list = numpy.random.randn(20)
theta_vals = sigma_theta*theta_list
print len(theta_vals)
length=10.0
step_length=1.0
diameter= 10e-6
test_fiber=fiber.LargeCoreMMF(length=length,step_length=step_length,a=diameter)
admissible_modes = test_fiber.admissible_modes
M = len(admissible_modes)
w = test_fiber.w
print w
offset_x = .5e-6*numpy.ones(20)
offset_y = .5e-6*numpy.ones(20)
print len(offset_x)
for K in range(20):
    test_fiber = fiber.GHModes(w, XX, YY, theta =0.0)
    test_fiber1 = fiber.GHModes(w,XX, YY, theta = theta_vals[K],offset_x = offset_x[K],offset_y = offset_y[K])
    E = []
    R = []
    for i in range(M):
        p, q = admissible_modes[i][0], admissible_modes[i][1]
        for j in range(M):
            m,n = admissible_modes[j][0], admissible_modes[j][1]
            mode_pattern_1 = test_fiber.get_mode_pattern(p,q)
            mode_pattern_2 = test_fiber1.get_mode_pattern(m,n)
            overlap = utils.overlap(mode_pattern_1, mode_pattern_2)
            E.append(overlap)
    A = numpy.array(E)
    O=numpy.sqrt(len(A))
    A1=A.reshape(O,O)
    A1= numpy.mat(A1)
    psi_matrix = numpy.kron(numpy.eye(2), A1)
    print K
    filename1='small core lossy projectiom matrix constant offset 05'+str(K)
    f1 = open(filename1,'w')
    pickle.dump(psi_matrix,f1)
    f1.close()
        
                
            
         
