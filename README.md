# Diploma Thesis, June 2022
## Abstract
The purpose of this Diploma Thesis is to study a new problem related to the limitation of misinformation spreading in a 
social network platform in combination with the simultaneous avoidance of the disturbance of the dissemination of true information, 
and the development of an efficient algorithm for its solution. 

The problem under consideration in this Thesis is the one of Cautious Misinformation Minimization (CMM) which is defined as minimizing
the spread of false information while minimizing the decrement of the spread of true information by limiting the interactions between 
the users, i.e., by removing a limited number of edges in the graph representing the network. Desiring the integration of user features 
in the evolution of information diffusion, the known Independent Cascade (IC) and Deterministic Linear Threshold (DLT) models are modified 
in this Thesis, in order to take into account the user's specialization in the thematic category to which the disseminated information belongs.
Under these models as well as the probabilistic Linear Threshold model (LT), the CMM problem is proved to be NP-Hard. Thus, to solve it under 
the LT and DLT models, greedy iterative algorithms are employed whose criterion for selecting the edge to be removed in each iteration is the 
maximum reduction of the sum of the difference between true information's current spread and its initial one, and false information's current spread.

The experimental evaluation of the proposed algorithms is carried out using real social networks. Their results are compared with the ones of the 
methods that utilize mainly topological features and partly the dynamic evolution of information dissemination. Based on these, the superiority 
of the proposed methods is highlighted since they achieve through the removal of a small number of edges the significant reduction of the spread 
of misinformation without greatly affecting the dissemination of true information.
