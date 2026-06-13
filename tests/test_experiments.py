def test_quantum_imports():
    """Test that Qiskit and our experiment files can be successfully imported."""
    import qiskit
    from experiments import superposition, entanglement
    
    assert callable(superposition.run_superposition_experiment)
    assert callable(entanglement.run_entanglement_experiment)
