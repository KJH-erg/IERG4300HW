import numpy as np
import matplotlib.pyplot as plt

reduce_dim = 64
num_viz_pca =64


def main():
    
    # load principle vectors from your local machine, e.g., here we suppose that the PCA vectors of the training
    # set is stored in a file named 'pca_components_20' in the ./mnist/ directory
    pv_dir = 'MNIST/pca_components_' + str(reduce_dim)
    pvs = np.empty((reduce_dim, 784))
    with open(pv_dir, 'r') as f:
        # Some pre-processing steps, depending on how you store your principle vectors
        # Here, we suppose that each row is corresponding to a principle vectors with string
        # type, e.g, a row can be: '0.5, 0.2, 0.3, ..., 0.21', each element is separated by ','.
        for k, line in enumerate(f.readlines()):
            line = line.strip().split(',')
            # the k-th principle vectors
            pv_k = np.array(list(map(float, line)))
            pvs [k] = pv_k
        #since we cannot show 64 vectors in one file I divided into 4 image files 16 each
        # cnt for the numbering of the image    
        lst = [0,16,32,48]
        cnt =0 
        for num_viz_pca in lst:

        # visualize the principle vectors
            fig, ax = plt.subplots( 16 // 4, 4)
            # YOU NEED TO FILL IN YOUR SID IN THE FOLLOWING LINE
            fig.suptitle('Visualization of Eigendigits ({})'.format('1155096482'))
            ax = ax.reshape(-1)
            for k, pv in enumerate(pvs [num_viz_pca:num_viz_pca+16]):
                pv = pv.reshape(28, 28)
                ax[k].imshow(pv, cmap='gray')
                ax[k].set_title('pv-{}'.format(cnt+1))
                ax[k].axis('off')
                cnt+=1

            fig.savefig('./viz_pca_vectors_{}.png'.format(num_viz_pca))


if __name__ == '__main__':
    main()