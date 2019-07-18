import numpy as np

seq1 = np.array([ 0.3, 0.6, 0.9 ])
seq2 = np.array([ [1,1], [2,3], [3,3] ])

n_samples = seq1.shape[0]
wrapper = np.zeros((n_samples, seq2.shape[1]))

print  wrapper.shape

# for i in xrange(n_samples):
#     wrapper[i,:] = seq1[i,:].dot(seq2[i,:]) / np.count_nonzero(seq1[i,:])
# wrapper  = seq1.dot(seq2)
print seq1.dot(seq2) # / np.count_nonzero(seq1)
# print seq1[0]