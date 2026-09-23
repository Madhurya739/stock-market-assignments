from src.analytics.clustering import run_clustering


def test_run_clustering_is_reproducible(sample_data):
    input_path, output_path = sample_data

    df1 = run_clustering(str(input_path), str(output_path))
    df2 = run_clustering(str(input_path), str(output_path))

    assert (df1["cluster"].values == df2["cluster"].values).all()
    assert (df1["archetype"].values == df2["archetype"].values).all()
