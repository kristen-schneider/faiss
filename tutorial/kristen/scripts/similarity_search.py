# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np
import faiss  # make faiss available

'''
    METRIC_INNER_PRODUCT = 0, ///< maximum inner product search
    METRIC_L2 = 1,            ///< squared L2 search
    METRIC_L1,                ///< L1 (aka cityblock)
    METRIC_Linf,              ///< infinity distance
    METRIC_Lp,                ///< L_p distance, p is given by a faiss::Index
                              /// metric_arg
'''
def inner_product(smf, queries, k):
    num_variants = len(smf[0])  # dimension

    # database to numpy
    numpy_smf = np.asarray(smf, dtype='float32')
    faiss.normalize_L2(numpy_smf)

    numpy_queries = np.asarray(queries, dtype='float32')

    index = faiss.IndexFlatIP(num_variants)

    print('Index is trained: ', index.is_trained)
    index.add(numpy_smf)  # add vectors to the index
    print('Number of samples: ', index.ntotal)

    print('Searching...')
    D, I = index.search(numpy_queries, k)  # actual search

    return I

def flatL2(smf, queries, k):
    num_variants = len(smf[0])            # dimension

    # database to numpy
    numpy_smf = np.asarray(smf, dtype='float32')
    numpy_queries = np.asarray(queries, dtype='float32')

    index = faiss.IndexFlatL2(num_variants)   # build the index
    print('Index is trained: ', index.is_trained)
    index.add(numpy_smf)                    # add vectors to the index
    print('Number of samples: ', index.ntotal)

    print('Searching...')
    D, I = index.search(numpy_queries, k)     # actual search
    print('indices:\n', I)
    # print('distances:\n', D)
    print('...search complete.')

    return I