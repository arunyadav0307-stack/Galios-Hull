#!/usr/bin/env python3
"""
Part 2 of the Nova Science Publishers book chapter content:
Sections 4, 5, 6, 7, and 8, numbered Display Equations (1)–(22), Tables 3–5,
Ethical & Editorial Declarations, Biographical Sketch Placeholder, and
28 100%-verified APA 7th edition references.
"""

EQUATIONS = {
    1: r"|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1",
    2: r"|\psi(\theta, \phi)\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle",
    3: r"|\Psi\rangle = {\sum_{x=0}^{2^n - 1} c_x |x\rangle}, \quad {\sum_{x=0}^{2^n - 1} |c_x|^2} = 1",
    4: r"\hat{\rho} = {\sum_{k} p_k |\psi_k\rangle\langle\psi_k|}, \quad \mathrm{Tr}(\hat{\rho}) = 1, \quad \mathrm{Tr}(\hat{\rho}^2) \leq 1",
    5: r"X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}",
    6: r"H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}, \quad T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}",
    7: r"R_\sigma(\theta) = \exp\left(-i\frac{\theta}{2}\sigma\right) = \cos\left(\frac{\theta}{2}\right)I - i\sin\left(\frac{\theta}{2}\right)\sigma",
    8: r"\mathrm{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}, \quad |\Phi^+\rangle = \frac{1}{\sqrt{2}}\left(|00\rangle + |11\rangle\right)",
    9: r"U_{\mathrm{circ}} = U_L U_{L-1} \cdots U_1, \quad \mathcal{E}(\hat{\rho}) = {\sum_{m} K_m \hat{\rho} K_m^\dagger}, \quad {\sum_{m} K_m^\dagger K_m} = I",
    10: r"p(m) = \mathrm{Tr}(\Pi_m \hat{\rho}), \quad \hat{\rho}_m = \frac{\Pi_m \hat{\rho} \Pi_m}{\mathrm{Tr}(\Pi_m \hat{\rho})}",
    11: r"\langle \hat{O} \rangle = \mathrm{Tr}(\hat{\rho}\hat{O}), \quad \mathrm{Var}(\hat{\mu}_M) = \frac{\langle \hat{O}^2 \rangle - \langle \hat{O} \rangle^2}{M}",
    12: r"\mathrm{QFT}_N |x\rangle = \frac{1}{\sqrt{N}} {\sum_{k=0}^{N-1} e^{2\pi i x k / N} |k\rangle}",
    13: r"A |x\rangle = |b\rangle, \quad |x\rangle = \frac{A^{-1}|b\rangle}{\|A^{-1}|b\rangle\|}, \quad Q_{\mathrm{HHL}} \in \tilde{O}\left(\frac{s^2 \kappa^2}{\epsilon}\right)",
    14: r"\min_{\boldsymbol{\theta} \in \mathbb{R}^K} E(\boldsymbol{\theta}) = \langle 0^{\otimes n} | U^\dagger(\boldsymbol{\theta}) \hat{H} U(\boldsymbol{\theta}) | 0^{\otimes n} \rangle \geq E_0",
    15: r"\frac{\partial E(\boldsymbol{\theta})}{\partial \theta_j} = \frac{1}{2}\left[ E\left(\boldsymbol{\theta} + \frac{\pi}{2}\mathbf{e}_j\right) - E\left(\boldsymbol{\theta} - \frac{\pi}{2}\mathbf{e}_j\right) \right]",
    16: r"\mathbb{E}_{\boldsymbol{\theta}}\left[\frac{\partial E(\boldsymbol{\theta})}{\partial \theta_j}\right] = 0, \quad \mathrm{Var}_{\boldsymbol{\theta}}\left[\frac{\partial E(\boldsymbol{\theta})}{\partial \theta_j}\right] \in O\left(\frac{1}{2^n}\right)",
    17: r"|\psi_p(\boldsymbol{\gamma}, \boldsymbol{\beta})\rangle = {\prod_{l=1}^{p} e^{-i\beta_l \hat{H}_B} e^{-i\gamma_l \hat{H}_C}} |+\rangle^{\otimes n}",
    18: r"\hat{H}_C = \frac{1}{2}{\sum_{(u,v)\in E} w_{uv}\left(I - Z_u Z_v\right)}, \quad \hat{H}_B = {\sum_{u \in V} X_u}",
    19: r"G^r |\psi_0\rangle = \sin\left((2r+1)\theta_0\right)|\psi_{\mathrm{good}}\rangle + \cos\left((2r+1)\theta_0\right)|\psi_{\mathrm{bad}}\rangle, \quad r^\star = \left\lfloor \frac{\pi}{4}\sqrt{\frac{N}{K_{\mathrm{sol}}}} \right\rfloor",
    20: r"K_Q(\mathbf{x}, \mathbf{x}^\prime) = |\langle \phi(\mathbf{x}) | \phi(\mathbf{x}^\prime) \rangle|^2 = |\langle 0^{\otimes n} | U_\Phi^\dagger(\mathbf{x}) U_\Phi(\mathbf{x}^\prime) | 0^{\otimes n} \rangle|^2",
    21: r"\mathrm{gen}(\boldsymbol{\theta}) = R(\boldsymbol{\theta}) - \hat{R}_S(\boldsymbol{\theta}) \in \tilde{O}\left(\sqrt{\frac{T}{S}}\right)",
    22: r"\varepsilon_d \propto \left(\frac{p}{p_{\mathrm{thr}}}\right)^{(d+1)/2} = \varepsilon_0 \Lambda^{-(d+1)/2}",
}

TABLES_PART2 = {
    3: {
        "caption": (
            "Table 3. Comparative taxonomy of core quantum algorithms for intelligent computing, "
            "highlighting hardware regime, theoretical guarantees, and dominant bottlenecks."
        ),
        "col_widths": [0.96, 0.72, 0.92, 0.95, 0.95],  # total = 4.50 inches exact
        "headers": ["Algorithm", "Regime", "Core Mechanism", "Theoretical Status", "Key Bottleneck"],
        "rows": [
            [
                "VQE / Variational Classifiers",
                "NISQ / Early FT",
                "Rayleigh–Ritz or empirical loss minimization via PQCs",
                "Heuristic; generalization O~(√(T/S))",
                "Barren plateaus, shot noise, local minima",
            ],
            [
                "QAOA",
                "NISQ / Early FT",
                "Alternating cost and mixer Hamiltonian trotterized layers",
                "Worst-case bounds at fixed p; heuristic scaling",
                "Deep p needed on dense graphs; gate noise",
            ],
            [
                "Grover / Amplitude Amplif.",
                "Fault-Tolerant",
                "Reflections in 2D subspace spanned by initial/target states",
                "Proven optimal quadratic speedup O(√(N/K))",
                "Oracle synthesis depth and QEC clock overhead",
            ],
            [
                "Quantum Kernel SVM",
                "NISQ / Fault-Tolerant",
                "Fidelity inner product in 2^n feature Hilbert space",
                "Proven exponential speedup on discrete-log data",
                "Kernel concentration; O(S^2) pair evaluations",
            ],
            [
                "HHL Linear Systems",
                "Fault-Tolerant",
                "QPE eigenvalue inversion and controlled ancilla rotation",
                "Proven O~(s^2 κ^2 / ε) under QRAM/sparsity",
                "State preparation, readout of full x, dequantization",
            ],
            [
                "QPE / Shor Subroutines",
                "Fault-Tolerant",
                "Coherent phase kickback and inverse QFT period finding",
                "Proven super-polynomial / exponential speedup",
                "Requires thousands of error-corrected logical qubits",
            ],
        ],
    },
    4: {
        "caption": (
            "Table 4. Asymptotic time/query complexity comparison between quantum subroutines "
            "and best known classical counterparts across canonical computational tasks."
        ),
        "col_widths": [1.05, 1.05, 1.05, 1.35],  # total = 4.50 inches exact
        "headers": ["Computational Task", "Best Classical Scaling", "Quantum Scaling", "Critical Caveats & Conditions"],
        "rows": [
            [
                "Unstructured search (N items, K=1)",
                "O(N) queries",
                "O(√N) queries (Grover, 1996)",
                "Provably optimal; practical win requires fast logical oracle",
            ],
            [
                "Integer factoring (n-bit integer N)",
                "exp(O(n^(1/3) (log n)^(2/3))) (GNFS)",
                "O(n^3) gates (Shor, 1997)",
                "Requires fault-tolerant logical qubits and modular arithmetic",
            ],
            [
                "Discrete-log kernel classification",
                "Super-polynomial (under DLP hardness)",
                "Polynomial time (Liu et al., 2021)",
                "Classical input vectors; requires fault-tolerant feature circuit",
            ],
            [
                "s-sparse linear system Ax = b",
                "O(N s κ log(1/ε)) (Conjugate Gradient)",
                "O~(s^2 κ^2 / ε) state prep (HHL, 2009)",
                "Outputs quantum state |x⟩, not all N entries; QRAM caveat",
            ],
            [
                "Low-rank matrix recommendation",
                "O(poly(k, log N)) (Tang, 2019)",
                "O(poly(k) polylog(N))",
                "Exponential speedup dequantized under l2-norm sampling",
            ],
            [
                "M observable shadows (n qubits)",
                "Exponential full state tomography",
                "O(log M) random measurements (Huang et al., 2020)",
                "Applies to bounded shadow-norm local/low-rank observables",
            ],
        ],
    },
    5: {
        "caption": (
            "Table 5. Synthesis of verified experimental and theoretical milestones published "
            "in peer-reviewed quantum computing literature."
        ),
        "col_widths": [0.95, 0.85, 1.25, 1.45],  # total = 4.50 inches exact
        "headers": ["Study", "Platform / Scope", "Task Investigated", "Verified Published Finding"],
        "rows": [
            [
                "Peruzzo et al. (2014)",
                "2-qubit photonic processor",
                "HeH+ molecular ground-state energy via VQE",
                "Demonstrated hybrid variational convergence resilient to systematic gate calibration errors",
            ],
            [
                "Havlíček et al. (2019)",
                "2-qubit superconducting chip",
                "Quantum variational classifier & kernel SVM",
                "Demonstrated experimental supervised classification on custom entangling feature spaces",
            ],
            [
                "Arute et al. (2019)",
                "53-qubit Sycamore transmon",
                "Random quantum circuit sampling (20 cycles)",
                "Sampled 2^53 state space at ~0.2% linear cross-entropy fidelity in 200 s hardware execution",
            ],
            [
                "Kim et al. (2023)",
                "127-qubit Eagle transmon",
                "2D transverse-field Ising Trotter dynamics",
                "Zero-noise extrapolation recovered accurate expectations up to 60 two-qubit gate layers",
            ],
            [
                "Acharya et al. (2025)",
                "105-qubit Willow transmon",
                "Distance-5 and distance-7 surface-code memory",
                "Below-threshold suppression factor Λ = 2.14 ± 0.02; 0.143% ± 0.003% error per cycle at d = 7",
            ],
        ],
    },
}

SECTIONS_PART2 = [
    {
        "num": "4",
        "title": "Quantum Circuits and Quantum Algorithmic Foundations",
        "subsections": [
            {
                "num": "4.1",
                "title": "Mathematical Representation of Qubits and Quantum States",
                "elements": [
                    ("p",
                     "In Dirac bra-ket notation, a pure single-qubit state is represented by a unit column vector "
                     "[[MATH: |\\psi\\rangle]] in a two-dimensional complex Hilbert space [[MATH: \\mathcal{H} \\cong \\mathbb{C}^2]] "
                     "with orthonormal computational basis [[MATH: |0\\rangle = (1, 0)^\\top]] and "
                     "[[MATH: |1\\rangle = (0, 1)^\\top]], conjugate transpose dual bras [[MATH: \\langle\\psi| = |\\psi\\rangle^\\dagger]], "
                     "and complex probability amplitudes [[MATH: \\alpha, \\beta \\in \\mathbb{C}]] satisfying Born normalization:"),
                    ("eq", 1),
                    ("p",
                     "Because global phase factors [[MATH: e^{i\\chi}|\\psi\\rangle]] ([[MATH: \\chi \\in \\mathbb{R}]]) "
                     "yield identical observable statistics, every pure single-qubit state maps bijectively (up to poles) "
                     "onto a point on the unit Bloch sphere parameterized by polar angle [[MATH: \\theta \\in [0, \\pi]]] "
                     "and azimuthal angle [[MATH: \\phi \\in [0, 2\\pi)]] (Nielsen & Chuang, 2010), as illustrated in Figure 1(a):"),
                    ("eq", 2),
                    ("p",
                     "For an [[MATH: n]]-qubit register, the composite Hilbert space is the [[MATH: 2^n]]-dimensional "
                     "tensor product [[MATH: \\mathcal{H}^{\\otimes n} \\cong \\mathbb{C}^{2^n}]] spanned by binary basis "
                     "kets [[MATH: |x\\rangle = |x_{n-1} \\cdots x_1 x_0\\rangle]] indexed by integers "
                     "[[MATH: x = \\sum_{q=0}^{n-1} x_q 2^q \\in \\{0, \\ldots, 2^n - 1\\}]] with amplitudes [[MATH: c_x \\in \\mathbb{C}]]:"),
                    ("eq", 3),
                    ("p",
                     "In realistic NISQ processors interacting with thermal and electromagnetic environments, states are "
                     "statistical ensembles or reduced subsystems described by a positive semidefinite Hermitian density "
                     "operator [[MATH: \\hat{\\rho} \\succeq 0]] generated by classical probabilities [[MATH: p_k \\geq 0]] "
                     "([[MATH: \\sum_k p_k = 1]]), where purity [[MATH: \\mathrm{Tr}(\\hat{\\rho}^2)]] equals [[MATH: 1]] "
                     "exclusively for pure states and decreases toward [[MATH: 1/2^n]] under decoherence:"),
                    ("eq", 4),
                ],
            },
            {
                "num": "4.2",
                "title": "Single-Qubit and Multi-Qubit Gates",
                "elements": [
                    ("p",
                     "Closed-system quantum gates act as unitary linear operators [[MATH: U \\in \\mathrm{U}(2^n)]] "
                     "satisfying [[MATH: U^\\dagger U = U U^\\dagger = I]]. Single-qubit algebra is anchored by the "
                     "identity [[MATH: I]] and the three Hermitian, unitary, traceless Pauli matrices [[MATH: X]], "
                     "[[MATH: Y]], and [[MATH: Z]], which satisfy [[MATH: \\sigma^2 = I]] for [[MATH: \\sigma \\in \\{X, Y, Z\\}]] "
                     "and generate the Lie algebra [[MATH: \\mathfrak{su}(2)]]:"),
                    ("eq", 5),
                    ("p",
                     "Discrete fault-tolerant synthesis relies on the Hadamard gate [[MATH: H]]—which maps [[MATH: |0\\rangle]] "
                     "to [[MATH: |+\\rangle = (|0\\rangle + |1\\rangle)/\\sqrt{2}]] and [[MATH: |1\\rangle]] to "
                     "[[MATH: |-\\rangle = (|0\\rangle - |1\\rangle)/\\sqrt{2}]]—alongside the Clifford phase gate "
                     "[[MATH: S]] and the non-Clifford [[MATH: \\pi/8]] gate [[MATH: T]]:"),
                    ("eq", 6),
                    ("p",
                     "Parameterized quantum circuits and hardware-native pulse compilers employ continuous rotation "
                     "operators [[MATH: R_\\sigma(\\theta)]] around axis [[MATH: \\sigma \\in \\{X, Y, Z\\}]] by rotation "
                     "angle [[MATH: \\theta \\in \\mathbb{R}]], enabling arbitrary [[MATH: \\mathrm{SU}(2)]] synthesis "
                     "via Euler decomposition [[MATH: U(\\alpha, \\beta, \\gamma) = R_z(\\alpha) R_y(\\beta) R_z(\\gamma)]]:"),
                    ("eq", 7),
                    ("p",
                     "Multi-qubit entanglement arises through conditional two-qubit gates. In the ordered basis "
                     "[[MATH: \\{|00\\rangle, |01\\rangle, |10\\rangle, |11\\rangle\\}]], [[MATH: \\mathrm{CNOT}]] flips "
                     "the target qubit conditioned on control state [[MATH: |1\\rangle]], mapping [[MATH: (H \\otimes I)|00\\rangle]] "
                     "to the maximally entangled Bell state [[MATH: |\\Phi^+\\rangle]] whose reduced single-qubit states "
                     "[[MATH: \\mathrm{Tr}_B(|\\Phi^+\\rangle\\langle\\Phi^+|) = I/2]] possess zero local bias yet maximal correlation:"),
                    ("eq", 8),
                ],
            },
            {
                "num": "4.3",
                "title": "Circuit Composition, Measurement and Readout",
                "elements": [
                    ("p",
                     "Parallel gates acting on disjoint registers combine via the Kronecker tensor product "
                     "[[MATH: U_A \\otimes U_B]], whereas sequential circuit layers one through [[MATH: L]] compose by "
                     "matrix multiplication in reverse chronological order. Under open-system NISQ noise, ideal unitary "
                     "evolution is replaced by a completely positive trace-preserving (CPTP) quantum channel "
                     "[[MATH: \\mathcal{E}(\\hat{\\rho})]] expressed via Kraus operators [[MATH: \\{K_m\\}]] (Nielsen & Chuang, 2010):"),
                    ("eq", 9),
                    ("p",
                     "Readout performs a projective measurement defined by complete orthogonal projectors "
                     "[[MATH: \\{\\Pi_m\\}]] satisfying [[MATH: \\Pi_m \\Pi_{m^\\prime} = \\delta_{mm^\\prime}\\Pi_m]] and "
                     "[[MATH: \\sum_m \\Pi_m = I]]. Outcome [[MATH: m]] occurs with Born probability [[MATH: p(m)]] and "
                     "projects the state onto [[MATH: \\hat{\\rho}_m]]:"),
                    ("eq", 10),
                    ("p",
                     "When estimating the expectation value of a Hermitian observable [[MATH: \\hat{O}]] across [[MATH: M]] "
                     "independent circuit executions (shots), the sample mean estimator [[MATH: \\hat{\\mu}_M]] is unbiased "
                     "with variance inversely proportional to [[MATH: M]], establishing an inescapable [[MATH: M = O(1/\\epsilon^2)]] "
                     "sampling cost for additive precision [[MATH: \\epsilon]] in standard NISQ readout (Tilly et al., 2022):"),
                    ("eq", 11),
                ],
            },
            {
                "num": "4.4",
                "title": "Quantum Circuit Design Principles",
                "elements": [
                    ("p",
                     "Effective circuit synthesis balances expressibility against compilation overhead and noise accumulation. "
                     "First, multi-controlled Boolean oracles require clean ancilla qubits that must be uncomputed via "
                     "inverse gate mirrors [[MATH: U_{\\mathrm{anc}}^\\dagger]] before final interference steps; residual "
                     "entanglement with garbage ancillas destroys off-diagonal coherence across computational branches "
                     "(Barenco et al., 1995; Nielsen & Chuang, 2010). Second, on superconducting heavy-hex or planar "
                     "grid processors with nearest-neighbor coupling, non-local two-qubit gates compile into chains of "
                     "[[MATH: \\mathrm{SWAP}]] gates—each costing three [[MATH: \\mathrm{CNOT}]] operations—making "
                     "hardware-native topology matching vital to bounding circuit error (Kim et al., 2023). Third, "
                     "preserving physical symmetries such as particle number (Hamming weight), time-reversal real "
                     "amplitudes, or graph permutation equivariance restricts parameterized evolution to compact "
                     "invariant subspaces, dramatically improving sample efficiency and trainability (Cerezo et al., 2021; "
                     "Cerezo et al., 2025). Fourth, gate cancellation passes and Cartan KAK two-qubit decompositions "
                     "compress arbitrary two-qubit unitaries into at most three [[MATH: \\mathrm{CNOT}]] gates plus "
                     "local single-qubit rotations, eliminating redundant entangling layers prior to hardware execution "
                     "(Barenco et al., 1995; Tilly et al., 2022)."),
                ],
            },
            {
                "num": "4.5",
                "title": "Representative Quantum Algorithms",
                "elements": [
                    ("p",
                     "Three foundational quantum subroutines underpin higher-level intelligent computing algorithms. "
                     "First, phase kickback converts oracle evaluations [[MATH: U_f |x\\rangle|-\\rangle = (-1)^{f(x)}|x\\rangle|-\\rangle]] "
                     "into relative phase patterns distinguishable in [[MATH: O(1)]] query on structured promises "
                     "(Deutsch, 1985; Nielsen & Chuang, 2010). Second, the Quantum Fourier Transform over [[MATH: N = 2^n]] "
                     "basis states maps computational basis state [[MATH: |x\\rangle]] coherently into frequency space "
                     "using only [[MATH: n(n+1)/2 = O(n^2)]] Hadamard and controlled-phase gates—an exponential gate "
                     "reduction relative to the [[MATH: O(n 2^n)]] classical Fast Fourier Transform—powering both Shor's "
                     "factoring algorithm (Shor, 1997) and QPE:"),
                    ("eq", 12),
                    ("p",
                     "Third, for a Hermitian [[MATH: s]]-sparse system [[MATH: A\\mathbf{x} = \\mathbf{b}]] of dimension "
                     "[[MATH: N]] with spectral condition number [[MATH: \\kappa = \\|A\\|\\,\\|A^{-1}\\|]], the HHL "
                     "algorithm (Harrow et al., 2009) combines QPE, ancilla rotation conditioned on reciprocal eigenvalues, "
                     "and QPE uncomputation to prepare normalized quantum state [[MATH: |x\\rangle]] to error [[MATH: \\epsilon]] "
                     "with query complexity [[MATH: Q_{\\mathrm{HHL}}]] polylogarithmic in [[MATH: N]], provided [[MATH: |b\\rangle]] "
                     "is efficiently preparable and only expectation observables [[MATH: \\langle x|\\hat{M}|x\\rangle]] "
                     "rather than all [[MATH: N]] vector components are required:"),
                    ("eq", 13),
                ],
            },
            {
                "num": "4.6",
                "title": "Computational Complexity and Resource Considerations",
                "elements": [
                    ("p",
                     "In computational complexity theory, the class of decision problems solvable with bounded error in "
                     "polynomial time by uniform families of quantum circuits is Bounded-Error Quantum Polynomial Time "
                     "([[MATH: \\mathrm{BQP}]]), which satisfies the containment hierarchy "
                     "[[MATH: \\mathrm{P} \\subseteq \\mathrm{BPP} \\subseteq \\mathrm{BQP} \\subseteq \\mathrm{PSPACE}]] "
                     "(Nielsen & Chuang, 2010; Montanaro, 2016). Integer factoring and discrete logarithms lie inside "
                     "[[MATH: \\mathrm{BQP} \\cap \\mathrm{NP} \\cap \\mathrm{coNP}]], supplying strong evidence that "
                     "[[MATH: \\mathrm{BQP}]] strictly exceeds classical probabilistic polynomial time [[MATH: \\mathrm{BPP}]]. "
                     "Crucially, however, complexity theorists widely conjecture [[MATH: \\mathrm{NP} \\not\\subseteq \\mathrm{BQP}]]: "
                     "quantum computers are not expected to solve arbitrary [[MATH: \\mathrm{NP}]]-complete combinatorial "
                     "problems in polynomial worst-case time, bounding generic unstructured combinatorial speedups to "
                     "polynomial (such as quadratic Grover) or heuristic improvements (Montanaro, 2016). In hardware "
                     "engineering, resource accounting further separates NISQ circuits—dominated by two-qubit gate "
                     "infidelity and shot overhead—from fault-tolerant circuits, where logical [[MATH: T]]-gate count "
                     "and magic-state distillation volume dominate spacetime cost."),
                ],
            },
        ],
    },
    {
        "num": "5",
        "title": "Quantum Algorithms in Intelligent Computing",
        "subsections": [
            {
                "num": "5.1",
                "title": "Variational Quantum Algorithms",
                "elements": [
                    ("p",
                     "Variational quantum algorithms (VQAs) cast eigenvalue estimation, combinatorial optimization, and "
                     "supervised learning as hybrid optimization over a [[MATH: K]]-parameter unitary ansatz "
                     "[[MATH: U(\\boldsymbol{\\theta})]] acting on [[MATH: |0^{\\otimes n}\\rangle]] (Peruzzo et al., 2014; "
                     "Cerezo et al., 2021; Tilly et al., 2022). Decomposing target Hamiltonian [[MATH: \\hat{H} = \\sum_{\\ell=1}^{J} c_\\ell \\hat{P}_\\ell]] "
                     "as a real linear combination of [[MATH: J = \\mathrm{poly}(n)]] Pauli strings [[MATH: \\hat{P}_\\ell \\in \\{I, X, Y, Z\\}^{\\otimes n}]], "
                     "the Rayleigh–Ritz variational principle guarantees an upper bound on ground-state energy [[MATH: E_0]]:"),
                    ("eq", 14),
                    ("p",
                     "When parameter [[MATH: \\theta_j]] enters gate [[MATH: U_j(\\theta_j) = \\exp(-i \\theta_j G_j / 2)]] "
                     "generated by an involutory Hermitian operator [[MATH: G_j^2 = I]] with unit vector [[MATH: \\mathbf{e}_j]], "
                     "exact analytic partial derivatives can be evaluated directly on hardware without finite-difference "
                     "step-size bias using the two-term parameter-shift identity (Mitarai et al., 2018; Cerezo et al., 2021):"),
                    ("eq", 15),
                    ("p",
                     "Despite exact differentiability, McClean et al. (2018) proved that whenever an ansatz of sufficient "
                     "depth approximates a unitary 2-design over [[MATH: \\mathrm{SU}(2^n)]], partial derivatives have zero "
                     "mean and exponentially small variance across parameter space, requiring [[MATH: \\Omega(2^n)]] "
                     "measurement shots per step merely to distinguish gradient sign from statistical shot noise:"),
                    ("eq", 16),
                ],
            },
            {
                "num": "5.2",
                "title": "Quantum Approximate Optimization Algorithm",
                "elements": [
                    ("p",
                     "Designed specifically for discrete combinatorial optimization, QAOA prepares a [[MATH: 2p]]-parameter "
                     "state [[MATH: |\\psi_p(\\boldsymbol{\\gamma}, \\boldsymbol{\\beta})\\rangle]] by alternating phase-separation "
                     "unitaries generated by diagonal problem Hamiltonian [[MATH: \\hat{H}_C]] with mixing unitaries "
                     "generated by non-commuting transverse-field Hamiltonian [[MATH: \\hat{H}_B]] acting on the uniform "
                     "superposition [[MATH: |+\\rangle^{\\otimes n} = H^{\\otimes n}|0\\rangle^{\\otimes n}]] (Farhi et al., 2014):"),
                    ("eq", 17),
                    ("p",
                     "For weighted MaxCut on graph [[MATH: G = (V, E)]] with edge weights [[MATH: w_{uv} \\geq 0]], "
                     "[[MATH: \\hat{H}_C]] and standard mixer [[MATH: \\hat{H}_B]] are expressed via Pauli-[[MATH: Z]] "
                     "correlations and single-qubit Pauli-[[MATH: X]] flips as follows:"),
                    ("eq", 18),
                    ("p",
                     "In the limit [[MATH: p \\to \\infty]], QAOA can trotterize adiabatic quantum evolution and converge "
                     "to global optima. At shallow constant depth [[MATH: p]], however, local causal light-cones "
                     "restrict correlations on sparse graphs, enabling classical algorithms such as Goemans–Williamson "
                     "semidefinite programming or local message-passing algorithms to match or exceed low-depth QAOA "
                     "approximation ratios on specific graph families, motivating warm-started and counterdiabatic QAOA "
                     "variants (Cerezo et al., 2021)."),
                ],
            },
            {
                "num": "5.3",
                "title": "Quantum Search and Amplitude Amplification",
                "elements": [
                    ("p",
                     "In unstructured search across [[MATH: N = 2^n]] candidates containing [[MATH: K_{\\mathrm{sol}} \\geq 1]] "
                     "valid solutions marked by phase oracle [[MATH: O_f |x\\rangle = (-1)^{f(x)}|x\\rangle]], Grover's "
                     "operator [[MATH: G = (2|\\psi_0\\rangle\\langle\\psi_0| - I) O_f]] rotates initial uniform state "
                     "[[MATH: |\\psi_0\\rangle = \\cos\\theta_0 |\\psi_{\\mathrm{bad}}\\rangle + \\sin\\theta_0 |\\psi_{\\mathrm{good}}\\rangle]] "
                     "by angle [[MATH: 2\\theta_0]] per iteration within the two-dimensional invariant subspace spanned by "
                     "unmarked superposition [[MATH: |\\psi_{\\mathrm{bad}}\\rangle]] and marked superposition "
                     "[[MATH: |\\psi_{\\mathrm{good}}\\rangle]], where [[MATH: \\sin\\theta_0 = \\sqrt{K_{\\mathrm{sol}}/N}]] "
                     "(Grover, 1996; Brassard et al., 2002):"),
                    ("eq", 19),
                    ("p",
                     "Within intelligent computing, amplitude amplification accelerates combinatorial branch-and-bound "
                     "search, satisfiability subroutines, k-nearest-neighbor distance minima, and Monte Carlo expectation "
                     "estimation—reducing sampling complexity from classical [[MATH: O(1/\\epsilon^2)]] to Heisenberg-limited "
                     "[[MATH: O(1/\\epsilon)]] under coherent fault-tolerant execution (Brassard et al., 2002; Montanaro, 2016)."),
                ],
            },
            {
                "num": "5.4",
                "title": "Quantum Machine Learning Algorithms",
                "elements": [
                    ("p",
                     "Quantum kernel methods map classical input vector [[MATH: \\mathbf{x} \\in \\mathbb{R}^d]] into pure "
                     "feature state [[MATH: |\\phi(\\mathbf{x})\\rangle = U_\\Phi(\\mathbf{x})|0^{\\otimes n}\\rangle]] "
                     "(or density operator [[MATH: \\hat{\\rho}(\\mathbf{x}) = |\\phi(\\mathbf{x})\\rangle\\langle\\phi(\\mathbf{x})|]]) "
                     "and evaluate positive definite fidelity kernel entries [[MATH: K_Q(\\mathbf{x}, \\mathbf{x}^\\prime)]] "
                     "via inversion tests or SWAP tests on quantum hardware before solving convex quadratic support-vector "
                     "dual programs classically (Havlíček et al., 2019; Huang et al., 2021):"),
                    ("eq", 20),
                    ("p",
                     "Crucially, Liu et al. (2021) proved an unconditional super-polynomial separation "
                     "over classical learners (under standard discrete-logarithm cryptographic hardness) using classical "
                     "input data mapped via Shor-type feature circuits on fault-tolerant hardware. For variational QML "
                     "models containing [[MATH: T]] trainable local gates trained on [[MATH: S]] independent data samples, "
                     "covering-number bounds establish that generalization error between true risk [[MATH: R(\\boldsymbol{\\theta})]] "
                     "and empirical risk [[MATH: \\hat{R}_S(\\boldsymbol{\\theta})]] scales favorably with gate count (Caro et al., 2022):"),
                    ("eq", 21),
                ],
            },
            {
                "num": "5.5",
                "title": "Hybrid Quantum-Classical Learning Architectures",
                "elements": [
                    ("p",
                     "Modern hybrid learning architectures extend basic variational classifiers in four directions: "
                     "(1) data re-uploading circuits that interleave feature encoding unitaries [[MATH: U_\\Phi(\\mathbf{x})]] "
                     "repeatedly with trainable layers to generate rich truncated Fourier series in input space (Cerezo "
                     "et al., 2021); (2) Quantum Convolutional Neural Networks (QCNNs) employing translational parameter "
                     "sharing and mid-circuit pooling measurements that maintain logarithmic depth and polynomial gradient "
                     "variance (Caro et al., 2022); (3) hybrid tensor-quantum pipelines where classical deep encoders "
                     "compress high-dimensional images or sequences into compact latent vectors matching qubit counts; and "
                     "(4) classical shadow learning, where randomized single-qubit Pauli or Clifford measurements convert "
                     "quantum states into classical descriptions capable of predicting [[MATH: M_{\\mathrm{obs}}]] bounded "
                     "observables from [[MATH: O(\\log M_{\\mathrm{obs}})]] experiments (Huang et al., 2020; Huang et al., 2021)."),
                ],
            },
            {
                "num": "5.6",
                "title": "Algorithm Selection and Practical Design Trade-Offs",
                "elements": [
                    ("p",
                     "Selecting an appropriate quantum algorithm requires balancing provable asymptotic scaling against "
                     "state-loading cost, circuit depth, shot overhead, and classical simulability (Montanaro, 2016; "
                     "Cerezo et al., 2025). Practitioners face four recurring engineering trade-offs. "
                     "First, an expressibility-versus-trainability trade-off governs variational ansatz design: deep "
                     "hardware-efficient circuits span high-dimensional regions of [[MATH: \\mathrm{SU}(2^n)]] but suffer "
                     "exponentially flat landscapes, whereas symmetry-preserving ansätze remain trainable yet must avoid "
                     "collapsing into classically simulable Lie subalgebras (McClean et al., 2018; Cerezo et al., 2025). "
                     "Second, an encoding-depth-versus-dimension trade-off separates amplitude encoding—which compresses "
                     "exponentially many classical features into n qubits at exponential gate synthesis "
                     "cost—from angle encoding, which loads d features in constant depth using O(d) "
                     "qubits or re-uploading layers. Third, an error-mitigation-versus-sampling trade-off governs NISQ "
                     "execution, since exponential variance blow-up limits unencoded circuit volume even when zero-noise "
                     "extrapolation eliminates first-order bias (Cai et al., 2023). Fourth, quadratic fault-tolerant "
                     "speedups must overcome logical clock-rate overheads relative to massively parallel classical GPUs. "
                     "Table 3 synthesizes these design trade-offs across the six principal algorithmic families."),
                    ("table", 3),
                ],
            },
        ],
    },
    {
        "num": "6",
        "title": "Applications, Results and Comparative Analysis",
        "subsections": [
            {
                "num": "6.1",
                "title": "Applications in Artificial Intelligence and Machine Learning",
                "elements": [
                    ("p",
                     "Across artificial intelligence, quantum algorithms target three distinct problem classes that differ "
                     "sharply in their evidentiary maturity. The highest-confidence class comprises learning over native "
                     "quantum data—such as classifying phases of matter from quantum sensors, learning Hamiltonians, "
                     "and characterizing molecular electronic structure—where quantum transducers or state preparation "
                     "avoid classical bit-loading bottlenecks altogether (Peruzzo et al., 2014; Huang et al., 2020; "
                     "Tilly et al., 2022). A second class targets structured algebraic learning tasks where feature "
                     "maps encode cryptographically hard group invariances inaccessible to polynomial classical kernels "
                     "(Liu et al., 2021). A third, exploratory class applies hybrid variational circuits and quantum "
                     "Born machines to generative modeling, reinforcement-learning policy approximation, and anomaly "
                     "detection on compact tabular datasets (Biamonte et al., 2017; Caro et al., 2022)."),
                ],
            },
            {
                "num": "6.2",
                "title": "Optimization, Classification and Pattern Recognition",
                "elements": [
                    ("p",
                     "In combinatorial optimization, QAOA and variational Ising formulations encode quadratic unconstrained "
                     "binary optimization (QUBO) instances arising in network routing, portfolio risk allocation, job-shop "
                     "scheduling, and graph partitioning onto diagonal spin Hamiltonians [[MATH: \\hat{H}_C]] (Farhi et al., "
                     "2014). Penalty multipliers enforce linear equality and inequality constraints directly within the "
                     "diagonal energy objective, although large penalty weights widen spectral range and tighten shot "
                     "precision requirements during classical parameter optimization (Cerezo et al., 2021). In supervised "
                     "classification and pattern recognition, fidelity quantum kernels and variational circuit classifiers "
                     "separate nonlinearly entangled decision boundaries in Hilbert space (Havlíček et al., 2019). "
                     "Critically, empirical research shows that generic feature maps applied without structural priors "
                     "to downsampled image or tabular benchmarks rarely outperform tuned radial-basis-function support "
                     "vector machines or gradient-boosted decision trees unless the quantum embedding mirrors underlying "
                     "data symmetry or projected local observables prevent exponential kernel concentration (Huang et al., "
                     "2021; Liu et al., 2021)."),
                ],
            },
            {
                "num": "6.3",
                "title": "Data Analysis and Decision Support",
                "elements": [
                    ("p",
                     "In quantitative decision support and risk analytics, fault-tolerant quantum amplitude estimation "
                     "accelerates Monte Carlo pricing, conditional value-at-risk estimation, and Bayesian inference by "
                     "achieving [[MATH: O(1/\\epsilon)]] query scaling relative to classical [[MATH: O(1/\\epsilon^2)]] "
                     "Monte Carlo sampling (Brassard et al., 2002; Montanaro, 2016). Similarly, sparse linear solvers "
                     "and spectral estimation subroutines support partial differential equation discretization and "
                     "network centrality analysis when matrix entries are computed on the fly by compact reversible "
                     "circuits rather than loaded from classical RAM (Harrow et al., 2009), avoiding the low-rank "
                     "classical dequantization regime identified by Tang (2019)."),
                ],
            },
            {
                "num": "6.4",
                "title": "Comparative Evaluation of Quantum and Classical Approaches",
                "elements": [
                    ("p",
                     "To synthesize when quantum algorithms genuinely outperform classical methods, Figure 4 contrasts "
                     "asymptotic operation scaling across canonical problem classes alongside a two-dimensional regime "
                     "decision matrix parameterized by circuit-depth tolerance and data structure. Three practical "
                     "decision principles emerge from this comparison. First, unstructured classical tabular, text, "
                     "and image workloads remain firmly within the classical GPU regime because state loading and shot "
                     "sampling outweigh shallow circuit expressibility gains. Second, tasks featuring compact symmetry-preserving "
                     "ansätze or direct quantum sensor inputs populate the pre-fault-tolerant hybrid regime when paired "
                     "with classical shadows and zero-noise extrapolation. Third, super-polynomial advantages in modular "
                     "arithmetic, high-condition-number sparse linear algebra, long-time quantum dynamics, and discrete-logarithm "
                     "kernels require fault-tolerant logical qubits operating below threshold. Table 4 complements "
                     "Figure 4 with exact asymptotic complexity bounds and operational caveats."),
                    ("figure", 4),
                    ("table", 4),
                ],
            },
            {
                "num": "6.5",
                "title": "Results from Verified Literature or Reproducible Experiments",
                "elements": [
                    ("p",
                     "Because this chapter conducts a critical synthesis rather than reporting new laboratory runs, "
                     "empirical evaluation rests strictly on verified peer-reviewed hardware and theoretical studies, "
                     "summarized in Table 5. Early proof-of-principle experiments validated VQE ground-state estimation "
                     "on photonic hardware (Peruzzo et al., 2014) and supervised quantum feature-space classification "
                     "on superconducting qubits (Havlíček et al., 2019). Arute et al. (2019) demonstrated random circuit "
                     "sampling across 53 transmon qubits in two hundred seconds, spurring both hardware "
                     "progress and vastly improved classical tensor-network simulators. At pre-fault-tolerant utility scale, "
                     "Kim et al. (2023) executed 127-qubit kicked-Ising circuits up to 60 two-qubit "
                     "gate layers using zero-noise extrapolation, while Acharya et al. (2025) demonstrated exponential "
                     "surface-code logical error suppression below threshold on the Willow superconducting processor. "
                     "Together, these milestone studies confirm steady progress across hardware generations while "
                     "reinforcing that careful classical baseline benchmarking remains indispensable before claiming "
                     "enduring computational advantage."),
                    ("table", 5),
                ],
            },
            {
                "num": "6.6",
                "title": "Scalability, Noise, Hardware Limitations and Practical Barriers",
                "elements": [
                    ("p",
                     "Scaling quantum intelligent computing confronts four concrete physical and algorithmic barriers. "
                     "First, gate errors, thermal relaxation ([[MATH: T_1]]), pure dephasing ([[MATH: T_2]]), crosstalk, "
                     "and readout assignment errors exponentially attenuate unmitigated expectation signals with circuit "
                     "volume. While quantum error mitigation protocols such as ZNE and PEC accurately remove estimator "
                     "bias at moderate depths, information-theoretic bounds prove that mitigation sampling variance "
                     "grows exponentially with circuit error count (Cai et al., 2023). Overcoming this barrier at scale "
                     "requires fault-tolerant quantum error correction, where encoding one logical qubit into "
                     "[[MATH: 2d^2 - 1]] physical qubits of a distance-[[MATH: d]] surface code exponentially suppresses "
                     "logical error per cycle [[MATH: \\varepsilon_d]] whenever physical error rate [[MATH: p]] lies "
                     "strictly below code threshold [[MATH: p_{\\mathrm{thr}}]], with error suppression factor "
                     "[[MATH: \\Lambda = \\varepsilon_d / \\varepsilon_{d+2} > 1]] (Acharya et al., 2025):"),
                    ("eq", 22),
                    ("p",
                     "Even under fault tolerance, logical clock speeds remain orders of magnitude slower than gigahertz "
                     "classical GPUs due to syndrome decoding latency and magic-state factories, meaning quadratic "
                     "speedups require large problem sizes to overcome constant-factor crossover overheads, whereas "
                     "super-polynomial speedups offer far more compelling practical crossover thresholds."),
                ],
            },
        ],
    },
    {
        "num": "7",
        "title": "Discussion and Future Directions",
        "subsections": [
            {
                "num": "7.1",
                "title": "Interpretation of the Main Findings",
                "elements": [
                    ("p",
                     "Synthesizing across Sections 2 through 6 yields a clear unifying principle: quantum computational "
                     "advantage in intelligent computing is neither universal nor automatic, but emerges exclusively where "
                     "quantum circuit structure aligns with intrinsic algebraic, combinatorial, or physical structure in "
                     "the computational task. Addressing RQ1 and RQ2, exponential Hilbert-space dimension [[MATH: 2^n]] "
                     "provides operational leverage only when paired with hardware-aware compilation, ancilla uncomputation, "
                     "and bounded shot variance (Barenco et al., 1995; Nielsen & Chuang, 2010). Addressing RQ3 and RQ4, "
                     "rigorous super-polynomial separations arise for group-structured feature spaces (Shor, 1997; Liu "
                     "et al., 2021), Hamiltonian simulation, and randomized shadow learning (Huang et al., 2020), whereas "
                     "unstructured deep ansätze confront either barren plateaus or classical simulability (McClean et al., "
                     "2018; Cerezo et al., 2025)."),
                ],
            },
            {
                "num": "7.2",
                "title": "Implications for Intelligent Computing",
                "elements": [
                    ("p",
                     "For artificial intelligence architects and systems engineers, quantum processing units should be "
                     "conceptualized not as standalone replacements for classical CPUs and GPUs, but as specialized "
                     "co-processors invoked selectively on structured kernels, sampling subroutines, and physical "
                     "simulation modules within heterogeneous workflows (Preskill, 2018; Cerezo et al., 2021). Near-term "
                     "value concentrates in learning directly from quantum sensors, accelerating molecular and materials "
                     "property screening, and warm-starting hybrid discrete optimization pipelines where classical neural "
                     "surrogates initialize compact quantum circuits near high-gradient regions."),
                ],
            },
            {
                "num": "7.3",
                "title": "Current Technical and Theoretical Limitations",
                "elements": [
                    ("p",
                     "Four substantive technical and theoretical limitations constrain immediate deployment. First, "
                     "hardware-realizable QRAM capable of coherent polylogarithmic access to large classical databases "
                     "remains unavailable at scale, restricting linear-algebraic speedups on raw big data (Biamonte et al., "
                     "2017; Tang, 2019). Second, NISQ error mitigation incurs exponential shot overhead as circuit volume "
                     "grows (Cai et al., 2023). Third, global loss landscapes, hardware noise, and excessive entanglement "
                     "induce barren plateaus across generic variational models (Larocca et al., 2025). Fourth, although "
                     "below-threshold surface-code logical memory has now been demonstrated experimentally (Acharya et al., "
                     "2025), scaling from isolated logical memories to hundreds of interacting fault-tolerant logical "
                     "qubits remains a multi-year engineering undertaking."),
                ],
            },
            {
                "num": "7.4",
                "title": "Research Opportunities and Future Directions",
                "elements": [
                    ("p",
                     "Four research trajectories offer high scientific leverage over the coming decade: "
                     "(1) early fault-tolerant algorithmic design that minimizes logical ancilla qubits and T-gate "
                     "depths through randomized compilation and linear combinations of unitaries; "
                     "(2) equivariant and physics-informed variational ansätze initialized via classical tensor networks "
                     "or graph neural surrogates within trainable basins (Caro et al., 2022; Cerezo et al., 2025); "
                     "(3) high-rate quantum low-density parity-check (qLDPC) codes and modular interconnects reducing "
                     "physical-to-logical qubit overhead substantially below planar surface-code [[MATH: 2d^2 - 1]] scaling; "
                     "and (4) reproducible community benchmarks evaluating wall-clock runtime, total shot budget, and "
                     "energy consumption against tuned classical GPU baselines."),
                ],
            },
        ],
    },
    {
        "num": "8",
        "title": "Conclusion",
        "subsections": [
            {
                "num": "8.1",
                "title": "Summary of Major Insights",
                "elements": [
                    ("p",
                     "This chapter established an integrated mathematical and architectural synthesis of quantum circuits "
                     "and quantum algorithms for intelligent computing across NISQ and fault-tolerant hardware regimes. Starting from Hilbert-space ket and density-operator "
                     "representations, universal Clifford+[[MATH: T]] and continuous rotation gates, CPTP noise channels, "
                     "and finite-shot readout variance, this chapter traced how circuit-level mechanics directly govern "
                     "VQE, QAOA, Grover amplitude amplification, HHL linear solvers, and quantum kernel classifiers."),
                ],
            },
            {
                "num": "8.2",
                "title": "Theoretical and Practical Implications",
                "elements": [
                    ("p",
                     "Theoretically, this synthesis demonstrates that expressibility, gradient trainability, generalization "
                     "capacity, data-loading depth, and classical simulability form a coupled system of constraints that "
                     "cannot be optimized one metric at a time. Practically, the six-stage design workflow, six-dimensional "
                     "evaluation framework, and regime-selection matrix provide researchers and practitioners with concrete "
                     "engineering criteria for matching problem structure to classical, error-mitigated NISQ, or "
                     "fault-tolerant quantum architectures."),
                ],
            },
            {
                "num": "8.3",
                "title": "Limitations of the Chapter",
                "elements": [
                    ("p",
                     "Three scope boundaries merit explicit acknowledgment. First, this chapter is a structured conceptual "
                     "and mathematical synthesis of peer-reviewed literature and reports no original quantum hardware "
                     "runs or simulated empirical datasets. Second, continuous-variable optical models, analog quantum "
                     "annealers, measurement-based cluster states, and topological computation fall outside primary focus. "
                     "Third, physical coherence times, two-qubit gate fidelities, and real-time syndrome decoding "
                     "latencies continue to advance rapidly across experimental hardware platforms."),
                ],
            },
            {
                "num": "8.4",
                "title": "Future Research Directions",
                "elements": [
                    ("p",
                     "Realizing durable, verifiable quantum utility across artificial intelligence and machine learning "
                     "will require co-designing structure-aware quantum circuits, low-overhead fault-tolerant error "
                     "correction, classical shadow interfaces, and transparent empirical benchmarks grounded in rigorous "
                     "complexity theory. Sustained collaboration across quantum physics, computer architecture, and "
                     "statistical learning will translate asymptotic theory into reliable intelligent systems."),
                ],
            },
        ],
    },
]

DECLARATIONS_SECTION = {
    "title": "Declarations and Editorial Disclosures",
    "paragraphs": [
        "Funding: [Placeholder — Specify external grant agencies and award numbers supporting this chapter, or state: "
        "'This research received no external funding.']",
        "Conflict of Interest: [Placeholder — Declare any financial or non-financial competing interests of the authors, "
        "or state: 'The authors declare no conflict of interest relevant to this chapter.']",
        "Research Ethics and Informed Consent: This chapter consists exclusively of mathematical analysis, conceptual "
        "synthesis, and critical evaluation of published peer-reviewed literature; no human participants, clinical data, "
        "or animal subjects were involved.",
        "Third-Party Permissions: All four figures (Figures 1–4) and all five tables (Tables 1–5) in this chapter are "
        "original author-created works prepared specifically for this manuscript; no previously published or copyrighted "
        "graphics or tables requiring third-party reproduction permissions are included.",
    ],
}

BIOGRAPHICAL_SKETCH_PLACEHOLDER = {
    "title": "Biographical Sketch (Author Placeholder — Per Nova Chapter Guidelines)",
    "fields": [
        ("Name:", "[First Name Middle Initial Last Name]"),
        ("Affiliation:", "[Department, University / Research Institute, City, State (if applicable), Country]"),
        ("Education:", "[Year–Year: Degree and Field, Institution, Country]"),
        ("Business Address:", "[Institutional Mailing Address — for Nova Biographical Sketch record only]"),
        ("Research and Professional Experience:", "[Concise summary of academic and research appointments]"),
        ("Professional Appointments:", "[Current academic rank, laboratory leadership, editorial service]"),
        ("Honors:", "[Fellowships, awards, academic distinctions]"),
        ("Publications from the Last 3 Years:", "[List selected peer-reviewed publications in APA style]"),
    ],
}

# 28 100%-verified APA 7th edition references (alphabetical by first author surname).
# Each tuple: (cite_key, authors_apa, year, title, venue_italic, vol_issue_pages, publisher_or_extra, doi_url)
VERIFIED_REFERENCES = [
    (
        "Acharya et al., 2025",
        "Acharya, R., Abanin, D. A., Aghababaie-Beni, L., Aleiner, I., Andersen, T. I., Ansmann, M., Arute, F., Arya, K., Asfaw, A., Astrakhantsev, N., Atalaya, J., Babbush, R., Bacon, D., Ballard, B., Bardin, J. C., Bausch, J., Bengtsson, A., Bilmes, A., Blackwell, S., ... Zobrist, N.",
        "2025",
        "Quantum error correction below the surface code threshold.",
        "Nature",
        ", 638(8052), 920–926.",
        "",
        "https://doi.org/10.1038/s41586-024-08449-y",
    ),
    (
        "Arute et al., 2019",
        "Arute, F., Arya, K., Babbush, R., Bacon, D., Bardin, J. C., Barends, R., Biswas, R., Boixo, S., Brandao, F. G. S. L., Buell, D. A., Burkett, B., Chen, Y., Chen, Z., Chiaro, B., Collins, R., Courtney, W., Dunsworth, A., Farhi, E., Foxen, B., ... Martinis, J. M.",
        "2019",
        "Quantum supremacy using a programmable superconducting processor.",
        "Nature",
        ", 574(7779), 505–510.",
        "",
        "https://doi.org/10.1038/s41586-019-1666-5",
    ),
    (
        "Barenco et al., 1995",
        "Barenco, A., Bennett, C. H., Cleve, R., DiVincenzo, D. P., Margolus, N., Shor, P., Sleator, T., Smolin, J. A., & Weinfurter, H.",
        "1995",
        "Elementary gates for quantum computation.",
        "Physical Review A",
        ", 52(5), 3457–3467.",
        "",
        "https://doi.org/10.1103/PhysRevA.52.3457",
    ),
    (
        "Biamonte et al., 2017",
        "Biamonte, J., Wittek, P., Pancotti, N., Rebentrost, P., Wiebe, N., & Lloyd, S.",
        "2017",
        "Quantum machine learning.",
        "Nature",
        ", 549(7671), 195–202.",
        "",
        "https://doi.org/10.1038/nature23474",
    ),
    (
        "Brassard et al., 2002",
        "Brassard, G., Høyer, P., Mosca, M., & Tapp, A.",
        "2002",
        "Quantum amplitude amplification and estimation. In S. J. Lomonaco Jr. & H. E. Brandt (Eds.), ",
        "Quantum computation and quantum information: A millennium volume",
        " (Vol. 305, pp. 53–74).",
        " American Mathematical Society.",
        "https://doi.org/10.1090/conm/305/05215",
    ),
    (
        "Cai et al., 2023",
        "Cai, Z., Babbush, R., Benjamin, S. C., Endo, S., Huggins, W. J., Li, Y., McClean, J. R., & O'Brien, T. E.",
        "2023",
        "Quantum error mitigation.",
        "Reviews of Modern Physics",
        ", 95(4), 045005.",
        "",
        "https://doi.org/10.1103/RevModPhys.95.045005",
    ),
    (
        "Caro et al., 2022",
        "Caro, M. C., Huang, H.-Y., Cerezo, M., Sharma, K., Sornborger, A., Cincio, L., & Coles, P. J.",
        "2022",
        "Generalization in quantum machine learning from few training data.",
        "Nature Communications",
        ", 13(1), 4919.",
        "",
        "https://doi.org/10.1038/s41467-022-32550-3",
    ),
    (
        "Cerezo et al., 2021",
        "Cerezo, M., Arrasmith, A., Babbush, R., Benjamin, S. C., Endo, S., Fujii, K., McClean, J. R., Mitarai, K., Yuan, X., Cincio, L., & Coles, P. J.",
        "2021",
        "Variational quantum algorithms.",
        "Nature Reviews Physics",
        ", 3(9), 625–644.",
        "",
        "https://doi.org/10.1038/s42254-021-00348-9",
    ),
    (
        "Cerezo et al., 2025",
        "Cerezo, M., Larocca, M., García-Martín, D., Diaz, N. L., Braccia, P., Fontana, E., Rudolph, M. S., Bermejo, P., Ijaz, A., Thanasilp, S., Anschuetz, E. R., & Holmes, Z.",
        "2025",
        "Does provable absence of barren plateaus imply classical simulability?",
        "Nature Communications",
        ", 16(1), 7907.",
        "",
        "https://doi.org/10.1038/s41467-025-63099-6",
    ),
    (
        "Deutsch, 1985",
        "Deutsch, D.",
        "1985",
        "Quantum theory, the Church–Turing principle and the universal quantum computer.",
        "Proceedings of the Royal Society of London. Series A, Mathematical and Physical Sciences",
        ", 400(1818), 97–117.",
        "",
        "https://doi.org/10.1098/rspa.1985.0070",
    ),
    (
        "Farhi et al., 2014",
        "Farhi, E., Goldstone, J., & Gutmann, S.",
        "2014",
        "A quantum approximate optimization algorithm.",
        "arXiv preprint arXiv:1411.4028",
        ".",
        "",
        "https://doi.org/10.48550/arXiv.1411.4028",
    ),
    (
        "Feynman, 1982",
        "Feynman, R. P.",
        "1982",
        "Simulating physics with computers.",
        "International Journal of Theoretical Physics",
        ", 21(6–7), 467–488.",
        "",
        "https://doi.org/10.1007/BF02650179",
    ),
    (
        "Grover, 1996",
        "Grover, L. K.",
        "1996",
        "A fast quantum mechanical algorithm for database search. In ",
        "Proceedings of the Twenty-Eighth Annual ACM Symposium on Theory of Computing",
        " (pp. 212–219).",
        " Association for Computing Machinery.",
        "https://doi.org/10.1145/237814.237866",
    ),
    (
        "Harrow et al., 2009",
        "Harrow, A. W., Hassidim, A., & Lloyd, S.",
        "2009",
        "Quantum algorithm for linear systems of equations.",
        "Physical Review Letters",
        ", 103(15), 150502.",
        "",
        "https://doi.org/10.1103/PhysRevLett.103.150502",
    ),
    (
        "Havlíček et al., 2019",
        "Havlíček, V., Córcoles, A. D., Temme, K., Harrow, A. W., Kandala, A., Chow, J. M., & Gambetta, J. M.",
        "2019",
        "Supervised learning with quantum-enhanced feature spaces.",
        "Nature",
        ", 567(7747), 209–212.",
        "",
        "https://doi.org/10.1038/s41586-019-0980-2",
    ),
    (
        "Huang et al., 2021",
        "Huang, H.-Y., Broughton, M., Mohseni, M., Babbush, R., Boixo, S., Neven, H., & McClean, J. R.",
        "2021",
        "Power of data in quantum machine learning.",
        "Nature Communications",
        ", 12(1), 2631.",
        "",
        "https://doi.org/10.1038/s41467-021-22539-9",
    ),
    (
        "Huang et al., 2020",
        "Huang, H.-Y., Kueng, R., & Preskill, J.",
        "2020",
        "Predicting many properties of a quantum system from very few measurements.",
        "Nature Physics",
        ", 16(10), 1050–1057.",
        "",
        "https://doi.org/10.1038/s41567-020-0932-7",
    ),
    (
        "Kim et al., 2023",
        "Kim, Y., Eddins, A., Anand, S., Wei, K. X., van den Berg, E., Rosenblatt, S., Nayfeh, H., Wu, Y., Zaletel, M., Temme, K., & Kandala, A.",
        "2023",
        "Evidence for the utility of quantum computing before fault tolerance.",
        "Nature",
        ", 618(7965), 500–505.",
        "",
        "https://doi.org/10.1038/s41586-023-06096-3",
    ),
    (
        "Larocca et al., 2025",
        "Larocca, M., Thanasilp, S., Wang, S., Sharma, K., Biamonte, J., Coles, P. J., Cincio, L., McClean, J. R., Holmes, Z., & Cerezo, M.",
        "2025",
        "Barren plateaus in variational quantum computing.",
        "Nature Reviews Physics",
        ", 7(4), 174–189.",
        "",
        "https://doi.org/10.1038/s42254-025-00813-9",
    ),
    (
        "Liu et al., 2021",
        "Liu, Y., Arunachalam, S., & Temme, K.",
        "2021",
        "A rigorous and robust quantum speed-up in supervised machine learning.",
        "Nature Physics",
        ", 17(9), 1013–1017.",
        "",
        "https://doi.org/10.1038/s41567-021-01287-z",
    ),
    (
        "McClean et al., 2018",
        "McClean, J. R., Boixo, S., Smelyanskiy, V. N., Babbush, R., & Neven, H.",
        "2018",
        "Barren plateaus in quantum neural network training landscapes.",
        "Nature Communications",
        ", 9(1), 4812.",
        "",
        "https://doi.org/10.1038/s41467-018-07090-4",
    ),
    (
        "Mitarai et al., 2018",
        "Mitarai, K., Negoro, M., Kitagawa, M., & Fujii, K.",
        "2018",
        "Quantum circuit learning.",
        "Physical Review A",
        ", 98(3), 032309.",
        "",
        "https://doi.org/10.1103/PhysRevA.98.032309",
    ),
    (
        "Montanaro, 2016",
        "Montanaro, A.",
        "2016",
        "Quantum algorithms: An overview.",
        "npj Quantum Information",
        ", 2(1), 15023.",
        "",
        "https://doi.org/10.1038/npjqi.2015.23",
    ),
    (
        "Nielsen & Chuang, 2010",
        "Nielsen, M. A., & Chuang, I. L.",
        "2010",
        "",
        "Quantum computation and quantum information: 10th anniversary edition",
        ".",
        " Cambridge University Press.",
        "https://doi.org/10.1017/CBO9780511976667",
    ),
    (
        "Peruzzo et al., 2014",
        "Peruzzo, A., McClean, J., Shadbolt, P., Yung, M.-H., Zhou, X.-Q., Love, P. J., Aspuru-Guzik, A., & O'Brien, J. L.",
        "2014",
        "A variational eigenvalue solver on a photonic quantum processor.",
        "Nature Communications",
        ", 5(1), 4213.",
        "",
        "https://doi.org/10.1038/ncomms5213",
    ),
    (
        "Preskill, 2018",
        "Preskill, J.",
        "2018",
        "Quantum computing in the NISQ era and beyond.",
        "Quantum",
        ", 2, 79.",
        "",
        "https://doi.org/10.22331/q-2018-08-06-79",
    ),
    (
        "Shor, 1997",
        "Shor, P. W.",
        "1997",
        "Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer.",
        "SIAM Journal on Computing",
        ", 26(5), 1484–1509.",
        "",
        "https://doi.org/10.1137/S0097539795293172",
    ),
    (
        "Tang, 2019",
        "Tang, E.",
        "2019",
        "A quantum-inspired classical algorithm for recommendation systems. In ",
        "Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing",
        " (pp. 217–228).",
        " Association for Computing Machinery.",
        "https://doi.org/10.1145/3313276.3316310",
    ),
    (
        "Tilly et al., 2022",
        "Tilly, J., Chen, H., Cao, S., Picozzi, D., Setia, K., Li, Y., Grant, E., Wossnig, L., Rungger, I., Booth, G. H., & Tennyson, J.",
        "2022",
        "The Variational Quantum Eigensolver: A review of methods and best practices.",
        "Physics Reports",
        ", 986, 1–128.",
        "",
        "https://doi.org/10.1016/j.physrep.2022.08.003",
    ),
]
