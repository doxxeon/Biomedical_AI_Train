import numpy as np

# 두 포인트 사이의 유클리드 거리 계산식을 구현합니다.
def dist(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))


def inertia(distances, cluster_labels):
    Inertia = 0
    for i,label in enumerate(cluster_labels):
        Inertia +=  distances[i, label]
    return Inertia

class KMeans:
    def __init__(self, K, max_iter =  100, random_state = 6):
        self.n_cluster = K
        self.max_iter = max_iter
        
        self.centroid = {}
        for i in range(K):
            self.centroid[i] = np.empty(shape = (1,2))
            
        self.Inertia = []
        self.random_state = random_state
    
    
    def fit(self, feature_data):
        
        x = feature_data
        
        ## Step 1: 군집 중심을 초기화합니다.
        centroid = {}
        
        np.random.seed(self.random_state)
        
        sampled_idx = np.random.randint(x.shape[0], size = self.n_cluster)
        
        for i, idx in enumerate(sampled_idx):
            self.centroid[i] = x[idx, :]
        
        for _ in range(self.max_iter):
            # Step 2 각 데이터 포인트로 부터, 군집의 중심까지의 유클리드 거리를 계산. 
            cluster = {}
            distances = []

            for i in range(x.shape[0]):
            
                d = []
                for c in self.centroid.values():
                    d.append( dist(x[i,:], c ))
                    
                
                cluster[i] = d.index(min(d))
                
                distances.append( np.array( [d]) )
            
            # Step 3 업데이트되어 할당된 군집을 기반으로 각 군집의 중심을 업데이트
            centroid = {}
            for i in range(self.n_cluster):
                centroid[i] = np.empty(shape = (1,2))
                
                samples_in_cl = [cl_id == i for cl_id in cluster.values()]
                sample_pool = x[samples_in_cl, :]
                
                if ( len( sample_pool) > 0 ):
                    centroid[i] = np.mean(sample_pool, 0)
                else:
                    centroid[i] = self.centroid[i]
                    
            # Step 4 Step2,3를 반복. 군집중심의 좌표에 변동이 없으면 중단합니다. 변동이 있는경우, 현 객체의 attribute: centroid와 cluster를 업데이트 된 centroid와 cluster로 변경합니다.
            
            if ( ( np.concatenate(list( self.centroid.values())) == np.concatenate(list( centroid.values())) ).all()):
                break
            else:
                self.centroid = centroid 
                self.cluster = cluster
                self.Inertia.append( inertia(np.concatenate(distances), list(cluster.values())) )
        return self