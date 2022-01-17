# lakeFS
---

- lakeFS is an **open source platform** that delivers resilience and manageability to **object-storage based data lakes.**
- lakeFS supports AWS S3, Azure Blob Storage and Google Cloud Storage (GCS)

### Features

- lakeFS provides a [Git-like branching and committing model](https://docs.lakefs.io/understand/branching-model.html) that scales to exabytes of data by utilizing S3, GCS, or Azure Blob for storage.
- Branching model makes your data lake ACID compliant

## Use-cases

- lakeFS enhances processing workflows at each step of the **data lifecycle**:

### **In Development**

- **Experiment** - try **new tools, upgrade versions, and evaluate code changes** in isolation. By **creating a branch of the data** you get an isolated snapshot to run experiments over, while others are not exposed. Compare between branches with different experiments or to the main branch of the repository to understand a change’s impact.
    - Data branch → isolate
- **Debug** - **checkout** specific commits in a repository’s commit history to materialize consistent, **historical versions of your data**. See the exact state of your data at the point-in-time of an error to understand its root cause. → Checkout, history 알 수 있음
- **Collaborate** - avoid managing data access at the two extremes of either 1) treating your data lake like a shared folder or 2) creating multiple copies of the data to safely collaborate. **Instead, leverage isolated branches managed by metadata (not copies of files) to work in parallel. →** Metadata에 의한 관리 (not file, folder) → parallel한 작업환경

### **During Deployment**

- **Version Control** - retain commits for a configurable duration, so **readers are able to query data** from the latest commit or any other point in time. Writers atomically introduce new data preventing inconsistent data views.
- **Test** - **define pre-merge and pre-commit hooks** to run tests that enforce schema and validate properties of the data to catch issues before they reach production. → Pre-xxx 라는 개념을 만들어서 commit전 test해볼 수 있도록 한듯

### **In Production**

- **Roll Back** - **recover from error**s by instantly **reverting data to a former,** consistent snapshot of the data lake. Choose any commit in a repository’s commit history to revert in one atomic action. → snapshot 일관성 유지하면서 roll back 가능
- **Troubleshoot** - investigate production errors by starting with a snapshot of the inputs to the failed process. Spend less time re-creating the state of datasets at the time of failure, and more time finding the solution. → troubleshoot 쉽다.
- **Cross-collection Consistency** - provide consumers multiple synchronized collections of data in one atomic, revertable action. Using branches, writers provide consistency guarantees across different logical collections - merging to the main branch only after all relevant datasets have been created or updated successfully.

## Reference
- https://lakefs.io/