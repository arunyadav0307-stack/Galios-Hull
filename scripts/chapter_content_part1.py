#!/usr/bin/env python3
"""
Part 1 of the Nova Science Publishers book chapter content:
Front matter, Abstract, Keywords, Sections 1, 2, and 3, plus Tables 1 and 2.
All inline math expressions are marked as [[MATH: ...]] and converted directly to native
Microsoft Word Equation Editor OMML (<m:oMath>) runs at build time.
"""

BOOK_METADATA = {
    "book_title": "Quantum Artificial Intelligence and Machine Learning: Principles, Algorithms, and Applications",
    "publisher": "Nova Science Publishers",
    "running_head": "Quantum Circuits and Quantum Algorithms",
    "chapter_title": "Quantum Circuits and Quantum Algorithms: Foundations, Design Principles, and Applications in Intelligent Computing",
    "authors_line": "[First Name M. Last Name], PhD* and [Second Author First Name M. Last Name], PhD",
    "affiliations": [
        "1Department of [Department Name], [University or Research Institution Name], [City], [State/Province if applicable], [Country]",
        "2Department of [Department Name], [University or Research Institution Name], [City], [State/Province if applicable], [Country]",
    ],
    "correspondence": "*Corresponding Author's Email: [corresponding.author@institution.edu]",
    "author_placeholder_note": (
        "[Editorial Note — Author Placeholders: Replace bracketed placeholders above with full author names "
        "(First Middle Last), highest doctoral or medical degree only (PhD or MD placed after surname; omit "
        "titles such as Professor, Dr., or Director), English institutional affiliations specifying City, State "
        "(where applicable), and Country without street addresses or postal codes, and active institutional email.]"
    ),
}

ABSTRACT_TEXT = (
    "Quantum computing offers a mathematically distinct model of information processing grounded in "
    "Hilbert-space state evolution, unitary gate synthesis, and projective measurement, motivating growing "
    "interest across artificial intelligence and machine learning. However, translating asymptotic quantum "
    "speedups into practical intelligent computing systems remains constrained by state-preparation overheads, "
    "barren optimization landscapes, hardware decoherence, and classical dequantization results. This chapter "
    "establishes a unified theoretical and engineering framework connecting foundational quantum circuit design "
    "principles to modern quantum and hybrid quantum-classical algorithms for optimization, search, kernel "
    "learning, and decision support. Using a structured literature synthesis, formal mathematical analysis, and "
    "comparative architectural evaluation, this chapter examines gate decompositions, variational ansätze, "
    "amplitude amplification, quantum feature maps, error mitigation, and fault-tolerant scaling laws. The "
    "synthesis demonstrates that credible quantum utility requires aligning problem algebraic structure with "
    "shallow symmetry-informed circuits or fault-tolerant logical architectures, providing researchers with "
    "rigorous criteria for algorithm selection and benchmarking."
)

KEYWORDS_LIST = [
    "quantum circuits",
    "quantum algorithms",
    "variational quantum algorithms",
    "quantum machine learning",
    "hybrid quantum-classical architectures",
    "quantum error mitigation",
]

TABLES_PART1 = {
    1: {
        "caption": (
            "Table 1. Canonical single-qubit and multi-qubit quantum gates, algebraic properties, "
            "and functional roles in intelligent computing circuits."
        ),
        "col_widths": [0.95, 0.68, 1.42, 1.45],  # total = 4.50 inches exact
        "headers": ["Gate Family", "Qubits", "Unitary Generator / Action", "Primary Algorithmic Role"],
        "rows": [
            [
                "Pauli (X, Y, Z)",
                "1",
                "Involutory bit/phase flips; Hermitian observables",
                "Basis preparation, stabilizer checks, Hamiltonian terms",
            ],
            [
                "Hadamard (H)",
                "1",
                "Maps computational basis to uniform superposition",
                "Interference setup in QFT, Grover, QPE, and kernels",
            ],
            [
                "Phase (S, T)",
                "1",
                "π/2 Clifford phase (S) and π/4 non-Clifford phase (T)",
                "Universal fault-tolerant synthesis with Clifford group",
            ],
            [
                "Parameterized (Rx, Ry, Rz)",
                "1",
                "Continuous SU(2) rotations exp(-iθσ/2)",
                "Angle data embedding and trainable variational weights",
            ],
            [
                "CNOT / CZ",
                "2",
                "Conditional bit-flip or conditional π phase kickback",
                "Entanglement generation in ansätze and surface codes",
            ],
            [
                "SWAP / iSWAP",
                "2",
                "Exchanges two-qubit states on coupled hardware graphs",
                "Topology routing on planar superconducting processors",
            ],
            [
                "Toffoli (CCX)",
                "3",
                "Doubly controlled NOT; universal reversible logic",
                "Arithmetic predicates, coherent lookup, Grover oracles",
            ],
        ],
    },
    2: {
        "caption": (
            "Table 2. Multidimensional evaluation framework for comparing quantum, hybrid, "
            "and classical intelligent computing algorithms."
        ),
        "col_widths": [1.02, 1.18, 1.15, 1.15],  # total = 4.50 inches exact
        "headers": ["Dimension", "Primary Metric", "NISQ Implications", "Fault-Tolerant Target"],
        "rows": [
            [
                "Space Overhead",
                "Physical vs. logical qubit count n",
                "50–1,000 noisy physical qubits without full QEC",
                "2d^2 - 1 physical qubits per surface-code logical qubit",
            ],
            [
                "Circuit Depth",
                "Two-qubit entangling gate layers L",
                "Restricted by T1/T2 coherence to O(10)–O(10^2) layers",
                "Polynomial logical depth sustained via syndrome decoding",
            ],
            [
                "Non-Clifford Cost",
                "Logical T-gate count and T-depth",
                "Absorbed into continuous native rotations with gate noise",
                "Dominant spacetime bottleneck via magic-state factories",
            ],
            [
                "Sampling Budget",
                "Measurement shots M and gradient evals",
                "Scales as O(1/ε^2); error mitigation inflates variance",
                "Coherent amplitude estimation reduces scaling toward O(1/ε)",
            ],
            [
                "Trainability",
                "Cost gradient variance Var[∂E/∂θ_j]",
                "Exponential barren plateaus under deep global ansätze",
                "Requires Lie-algebraic or symmetry-constrained structure",
            ],
            [
                "Data I/O Model",
                "Encoding depth or oracle calls",
                "Classical feature loading can dominate wall-clock runtime",
                "Speedups require compact data or efficient circuit synthesis",
            ],
        ],
    },
}

SECTIONS_PART1 = [
    {
        "num": "1",
        "title": "Introduction",
        "subsections": [
            {
                "num": "1.1",
                "title": "Background and Motivation",
                "elements": [
                    ("p",
                     "Modern intelligent computing systems rely on classical von Neumann and tensor-accelerator "
                     "architectures whose empirical effectiveness across statistical learning and combinatorial "
                     "optimization scales with parallel hardware throughput. Fundamental bottlenecks nevertheless "
                     "arise when problem instances induce exponentially large state spaces, strongly correlated "
                     "quantum many-body structure, or intractable group-theoretic operations. Quantum computing "
                     "replaces Boolean bit registers with state vectors and density operators defined on complex "
                     "Hilbert spaces, evolving coherently under reversible unitary circuits prior to probabilistic "
                     "projective measurement (Feynman, 1982; Deutsch, 1985; Nielsen & Chuang, 2010). Rather than "
                     "accelerating arbitrary classical workloads indiscriminately, quantum processors achieve speedups "
                     "only when wave interference amplifies target solution amplitudes more efficiently than classical "
                     "randomized or heuristic algorithms (Biamonte et al., 2017). Two hardware regimes now shape research: "
                     "noisy intermediate-scale quantum (NISQ) processors executing shallow error-mitigated hybrid "
                     "circuits (Preskill, 2018; Kim et al., 2023; Cai et al., 2023) and emerging early fault-tolerant "
                     "architectures demonstrating below-threshold surface-code logical memories (Acharya et al., 2025)."),
                ],
            },
            {
                "num": "1.2",
                "title": "Research Problem and Significance",
                "elements": [
                    ("p",
                     "A persistent conceptual divide separates formal quantum algorithm theory from applied machine "
                     "learning engineering. Foundational complexity proofs frequently assume fault-tolerant logical "
                     "qubits, idealized black-box oracles, or cost-free quantum random access memory (QRAM), obscuring "
                     "state-preparation and readout bottlenecks that dominate end-to-end runtime (Harrow et al., 2009; "
                     "Biamonte et al., 2017). Conversely, heuristic studies of parameterized quantum circuits often "
                     "treat variational ansätze as drop-in replacements for classical neural networks, overlooking "
                     "exponentially vanishing barren-plateau gradients (McClean et al., 2018), quantum-inspired "
                     "classical dequantization of low-rank linear algebra (Tang, 2019), and inner-product concentration "
                     "in generic quantum kernels (Cerezo et al., 2025). Without unified architectural guidance connecting "
                     "physical gate synthesis to statistical learning theory, practitioners risk misallocating quantum "
                     "resources to tasks where classical tensor networks or gradient-boosted ensembles perform faster, "
                     "cheaper, and more reliably. Bridging low-level circuit mechanics with rigorous complexity bounds "
                     "is therefore critical for identifying genuine utility."),
                ],
            },
            {
                "num": "1.3",
                "title": "Objectives and Research Questions",
                "elements": [
                    ("p",
                     "The objective of this chapter is to establish a mathematically rigorous, engineering-oriented "
                     "synthesis linking quantum circuit design principles to quantum algorithms for intelligent "
                     "computing. Specifically, this chapter addresses four research questions: (RQ1) How do Hilbert-space "
                     "state representations, universal gate decompositions, and projective measurement statistics "
                     "govern the expressive capacity and shot complexity of quantum circuits? (RQ2) Which structural "
                     "compilation principles enable hardware efficiency, symmetry preservation, and error suppression "
                     "across NISQ and fault-tolerant regimes? (RQ3) Under what formal assumptions do variational "
                     "algorithms, QAOA, amplitude amplification, linear-system solvers, and quantum kernels achieve "
                     "provable or empirically credible advantages over classical baselines? (RQ4) How should hybrid "
                     "quantum-classical architectures be designed and benchmarked to navigate barren plateaus and noise?"),
                ],
            },
            {
                "num": "1.4",
                "title": "Scope and Contributions of the Chapter",
                "elements": [
                    ("p",
                     "This chapter focuses on gate-based digital quantum computation and hybrid quantum-classical "
                     "learning and optimization workflows, referencing analog annealing or continuous-variable "
                     "photonics only for boundary contrast. Four principal contributions distinguish this chapter: "
                     "(1) a unified operator-theoretic formulation connecting pure states, open-system density matrices, "
                     "universal gate sets, and finite-shot measurement variance; (2) an end-to-end circuit synthesis "
                     "and execution methodology spanning both error-mitigated NISQ and surface-code fault-tolerant "
                     "regimes; (3) rigorous mathematical derivations and side-by-side comparisons of core intelligent "
                     "computing algorithms that separate proven complexity separations from heuristic proposals; and "
                     "(4) a critical synthesis of verified published benchmarks and practical selection trade-offs."),
                ],
            },
            {
                "num": "1.5",
                "title": "Organization of the Chapter",
                "elements": [
                    ("p",
                     "Section 2 reviews foundational literature across quantum computation, circuit synthesis, quantum "
                     "machine learning, and open research gaps. Section 3 details the analytical methodology of this "
                     "chapter, circuit representation conventions, hybrid execution workflows, evaluation criteria, "
                     "and reproducibility assumptions. Section 4 formalizes qubit state spaces, single- and multi-qubit "
                     "unitary gates, open-system readout, foundational subroutines, and complexity classes. Section 5 "
                     "analyzes variational quantum algorithms, QAOA, quantum search, quantum kernels, generalization "
                     "bounds, and hybrid architectures. Section 6 evaluates applications, published empirical and "
                     "theoretical benchmarks, and hardware scaling barriers. Sections 7 and 8 synthesize implications, "
                     "limitations, future research opportunities, and concluding insights."),
                ],
            },
        ],
    },
    {
        "num": "2",
        "title": "Literature Review and Theoretical Foundations",
        "subsections": [
            {
                "num": "2.1",
                "title": "Fundamentals of Quantum Computing",
                "elements": [
                    ("p",
                     "Feynman (1982) first observed that classical computers incur exponential memory and runtime costs "
                     "when simulating local quantum many-body dynamics, motivating controllable quantum systems as "
                     "computational substrates. Deutsch (1985) formalized the universal quantum Turing machine, while "
                     "subsequent circuit theory established networks of reversible unitary gates acting on multi-qubit "
                     "registers as the canonical operational model (Nielsen & Chuang, 2010). Closed-system evolution "
                     "is linear, norm-preserving, and unitary, forbidding fan-out state cloning via the no-cloning "
                     "theorem and requiring ancilla uncomputation for non-bijective Boolean logic. Furthermore, "
                     "Holevo's bound proves that projective measurement of [[MATH: n]] qubits extracts at most "
                     "[[MATH: n]] classical bits per shot despite the [[MATH: 2^n]]-dimensional state vector, implying "
                     "that useful algorithms must concentrate amplitude onto target outcomes via wave interference."),
                ],
            },
            {
                "num": "2.2",
                "title": "Qubits, Superposition and Entanglement",
                "elements": [
                    ("p",
                     "A physical qubit encodes information within two isolated energy or polarization levels spanning "
                     "[[MATH: \\mathcal{H} \\cong \\mathbb{C}^2]], realized experimentally across superconducting "
                     "transmon circuits (Arute et al., 2019; Acharya et al., 2025), trapped ions, neutral atom arrays, "
                     "and integrated photonics (Peruzzo et al., 2014). Superposition enables coherent phase encoding "
                     "within single registers, whereas non-factorizable multi-qubit states in "
                     "[[MATH: \\mathcal{H}^{\\otimes n} \\cong \\mathbb{C}^{2^n}]] exhibit quantum entanglement "
                     "(Nielsen & Chuang, 2010). Product-state circuits and pure Clifford stabilizer circuits remain "
                     "efficiently simulable on classical computers via tensor contractions or the Gottesman–Knill "
                     "theorem, making non-Clifford magic and multipartite entanglement necessary resources for quantum "
                     "speedups. Paradoxically, however, excessive volume-law entanglement in deep variational circuits "
                     "thermalizes local reduced states toward maximally mixed ensembles, inducing untrainable barren "
                     "plateaus (McClean et al., 2018; Cerezo et al., 2025)."),
                ],
            },
            {
                "num": "2.3",
                "title": "Quantum Gates and Quantum Circuits",
                "elements": [
                    ("p",
                     "Barenco et al. (1995) proved that arbitrary single-qubit rotations combined with two-qubit "
                     "Controlled-NOT ([[MATH: \\mathrm{CNOT}]]) gates form an exact universal basis for all unitaries "
                     "in [[MATH: \\mathrm{U}(2^n)]]. For fault-tolerant architectures, the discrete Clifford+[[MATH: T]] "
                     "library—comprising Hadamard ([[MATH: H]]), phase ([[MATH: S]]), [[MATH: \\mathrm{CNOT}]], and "
                     "[[MATH: T]] gates—approximates arbitrary single-qubit unitaries within operator norm [[MATH: \\epsilon]] "
                     "using [[MATH: O(\\log^c(1/\\epsilon))]] gates via the Solovay–Kitaev theorem and optimal Ross–Selinger "
                     "synthesis (Nielsen & Chuang, 2010). Figure 1 depicts the single-qubit Bloch sphere, a canonical "
                     "three-qubit entangling circuit with classical readout, and the four-tier execution architecture. "
                     "Table 1 catalogs canonical gate families and their algorithmic functions."),
                    ("figure", 1),
                    ("table", 1),
                ],
            },
            {
                "num": "2.4",
                "title": "Quantum Algorithms: Historical Development and Core Principles",
                "elements": [
                    ("p",
                     "Early oracle results such as the Deutsch–Jozsa problem demonstrated exponential query separations "
                     "over deterministic classical algorithms via phase kickback (Deutsch, 1985; Nielsen & Chuang, 2010). "
                     "Shor (1997) transformed coherent interference into polynomial-time algorithms for integer "
                     "factorization and discrete logarithms using modular exponentiation and the Quantum Fourier "
                     "Transform (QFT). Concurrently, Grover (1996) derived an optimal [[MATH: O(\\sqrt{N})]] unstructured "
                     "search algorithm generalized by Brassard et al. (2002) into universal amplitude amplification and "
                     "estimation. Harrow et al. (2009) extended quantum phase estimation (QPE) to sparse linear systems "
                     "(HHL), preparing states proportional to [[MATH: A^{-1}\\mathbf{b}]]. To accommodate limited NISQ "
                     "coherence, Peruzzo et al. (2014) and Farhi et al. (2014) introduced variational eigensolvers (VQE) "
                     "and QAOA, coupling shallow parameterized circuits to classical optimizers (Cerezo et al., 2021; "
                     "Tilly et al., 2022)."),
                ],
            },
            {
                "num": "2.5",
                "title": "Quantum Machine Learning and Intelligent Computing",
                "elements": [
                    ("p",
                     "Quantum machine learning encompasses fault-tolerant linear-algebraic accelerators (Biamonte et al., "
                     "2017), differentiable parameterized quantum circuits trained via analytic parameter-shift rules "
                     "(Mitarai et al., 2018), and quantum kernel methods mapping classical inputs into feature Hilbert "
                     "spaces (Havlíček et al., 2019). Foundational statistical learning theory further characterizes "
                     "circuit expressibility and inductive bias (Cerezo et al., 2021), randomized shadow tomography "
                     "(Huang et al., 2020), provable discrete-logarithm kernel separations (Liu et al., 2021), and "
                     "finite-sample generalization error scaling as [[MATH: \\tilde{O}(\\sqrt{T/S})]] for [[MATH: T]] "
                     "trainable gates across [[MATH: S]] training examples (Caro et al., 2022)."),
                ],
            },
            {
                "num": "2.6",
                "title": "Critical Review of Existing Research",
                "elements": [
                    ("p",
                     "Rigorous scrutiny has overturned several overly broad claims in early QML research. Tang (2019) "
                     "proved that quantum-inspired classical sampling algorithms match polylogarithmic quantum runtimes "
                     "for low-rank recommendation and matrix tasks when given comparable [[MATH: \\ell_2]]-sampling "
                     "access, eliminating putative exponential speedups on unstructured classical matrices. McClean "
                     "et al. (2018) established that expressive random ansätze suffer exponential gradient decay, "
                     "extended by subsequent work to global observables, entanglement-induced thermalization, and "
                     "hardware noise (Cerezo et al., 2021). Crucially, Cerezo et al. (2025) demonstrated that many "
                     "architectures proven immune to barren plateaus evolve within polynomial-dimension Lie algebras "
                     "or shallow causal cones that remain classically simulable unless initialized from non-trivial "
                     "quantum states."),
                ],
            },
            {
                "num": "2.7",
                "title": "Research Gaps and Conceptual Foundations",
                "elements": [
                    ("p",
                     "Four gaps persist across applied studies: (1) omitting state-preparation and shot overheads "
                     "when claiming asymptotic speedups; (2) extrapolating [[MATH: 4]]- to [[MATH: 12]]-qubit noiseless "
                     "simulations where barren plateaus remain invisible; (3) conflating exponential-overhead NISQ "
                     "error mitigation (Cai et al., 2023) with scalable fault-tolerant error correction (Acharya et al., "
                     "2025); and (4) lacking systematic decision rules matching data structure to circuit depth. "
                     "Addressing these four gaps forms the conceptual foundation of this chapter."),
                ],
            },
        ],
    },
    {
        "num": "3",
        "title": "Research Methodology and Design Framework",
        "subsections": [
            {
                "num": "3.1",
                "title": "Research Approach and Chapter Method",
                "elements": [
                    ("p",
                     "This chapter adopts a structured conceptual synthesis combined with formal linear-algebraic "
                     "derivation and comparative architectural analysis. No new laboratory quantum hardware runs or "
                     "synthetic empirical benchmarks are fabricated or claimed, nor is a bibliometric PRISMA review "
                     "asserted. Instead, archival theoretical proofs and verified experimental hardware milestones "
                     "are synthesized under uniform mathematical notation to evaluate circuit expressibility, gradient "
                     "trainability, sample complexity, and noise scaling on equal footing."),
                ],
            },
            {
                "num": "3.2",
                "title": "Quantum Circuit Representation and Design Principles",
                "elements": [
                    ("p",
                     "Quantum circuits in this chapter are modeled as left-to-right directed acyclic networks over "
                     "[[MATH: n]] quantum wires initialized in [[MATH: |0\\rangle^{\\otimes n}]] and classical readout "
                     "registers (Nielsen & Chuang, 2010). Four design rules govern synthesis: (1) reversible ancilla "
                     "uncomputation back to [[MATH: |0\\rangle]] to prevent unintended entanglement decoherence; "
                     "(2) hardware-aware gate compilation minimizing two-qubit [[MATH: \\mathrm{CNOT}/\\mathrm{CZ}]] "
                     "layers and [[MATH: \\mathrm{SWAP}]] routing overhead on planar topologies (Barenco et al., 1995); "
                     "(3) symmetry-informed inductive bias constraining ansätze to problem-invariant subspaces "
                     "(Cerezo et al., 2021; Cerezo et al., 2025); and (4) measurement parsimony via commuting Pauli grouping "
                     "or classical shadows (Huang et al., 2020; Tilly et al., 2022)."),
                ],
            },
            {
                "num": "3.3",
                "title": "Quantum Algorithm Design and Execution Workflow",
                "elements": [
                    ("p",
                     "Figure 2 formalizes the six-stage design and execution workflow used throughout this chapter. "
                     "Problem specifications (Stage 1: cost Hamiltonians [[MATH: \\hat{H}_C]], Boolean oracles, or "
                     "labeled datasets) are mapped into quantum encoding and algorithmic structures (Stage 2) and "
                     "transpiled into hardware-native gate sequences (Stage 3). Execution then bifurcates by hardware "
                     "regime: pre-fault-tolerant NISQ execution (Stage 4a) restricts depth within relaxation times "
                     "[[MATH: T_1, T_2]] and applies statistical error mitigation such as zero-noise extrapolation "
                     "(ZNE) and probabilistic error cancellation (PEC) (Kim et al., 2023; Cai et al., 2023), whereas "
                     "fault-tolerant execution (Stage 4b) encodes logical qubits in surface codes with real-time "
                     "syndrome decoding and magic-state [[MATH: T]]-gate distillation (Acharya et al., 2025). Both "
                     "paths feed shot-based expectation estimation and parameter updates (Stage 5) before rigorous "
                     "comparison against state-of-the-art classical solvers (Stage 6)."),
                    ("figure", 2),
                ],
            },
            {
                "num": "3.4",
                "title": "Quantum-Classical Hybrid Architectures",
                "elements": [
                    ("p",
                     "Contemporary intelligent computing predominantly relies on tightly coupled hybrid architectures "
                     "partitioning workload by physical strength (Peruzzo et al., 2014; Cerezo et al., 2021). As "
                     "depicted in Figure 3, a classical CPU/GPU co-processor performs feature scaling, principal "
                     "component compression, loss evaluation, and parameter updates, while the QPU executes state "
                     "embedding [[MATH: U_\\Phi(\\tilde{\\mathbf{x}})]], parameterized evolution "
                     "[[MATH: U_{\\mathrm{var}}(\\boldsymbol{\\theta}^{(t)})]], and [[MATH: M]]-shot observable sampling "
                     "returning empirical means [[MATH: \\hat{\\mu}_k \\pm \\sigma/\\sqrt{M}]] for analytic parameter-shift "
                     "or stochastic optimization (Mitarai et al., 2018; Tilly et al., 2022)."),
                    ("figure", 3),
                ],
            },
            {
                "num": "3.5",
                "title": "Evaluation Metrics and Comparison Criteria",
                "elements": [
                    ("p",
                     "Credible algorithmic comparison requires evaluating six orthogonal metrics simultaneously rather "
                     "than citing noiseless gate counts in isolation (Tilly et al., 2022; Cai et al., 2023). First, qubit footprint must separate unencoded physical qubits from error-corrected logical "
                     "qubits together with routing ancillas. Second, circuit depth must count sequential entangling "
                     "two-qubit gate layers after transpilation onto the target device coupling graph rather than "
                     "pre-compilation abstract unitaries. Third, non-Clifford resource cost tracks logical [[MATH: T]]-gate "
                     "count and [[MATH: T]]-depth, which dictate magic-state factory overhead in fault-tolerant systems. "
                     "Fourth, total shot complexity accounts for all repeated circuit executions summed across every "
                     "observable term, gradient evaluation, and error-mitigation noise scale factor. Fifth, trainability "
                     "tracks cost-gradient variance scaling with system width [[MATH: n]]. Sixth, end-to-end data I/O "
                     "accounts for state-preparation depth relative to classical memory bandwidth. Table 2 summarizes "
                     "these six evaluation criteria across NISQ and fault-tolerant execution regimes."),
                    ("table", 2),
                ],
            },
            {
                "num": "3.6",
                "title": "Assumptions, Constraints and Reproducibility",
                "elements": [
                    ("p",
                     "Every analysis in this chapter explicitly distinguishes three physical models: (1) closed-system "
                     "ideal unitary mechanics; (2) open-system NISQ channels subject to depolarizing, amplitude-damping, "
                     "and readout noise under finite shot budgets [[MATH: M]]; and (3) fault-tolerant logical circuits "
                     "operating below code threshold [[MATH: p < p_{\\mathrm{thr}}]]. Reproducible reporting requires "
                     "specifying native gate sets, transpiled two-qubit depth, total shots across all optimization "
                     "steps, error-mitigation scale factors, random seeds, and tuned classical baseline implementations."),
                ],
            },
        ],
    },
]
