## DVC

- command line tool like git
- Data versioning 관리 + model pipeline 등 (일반적으로 data versioning에만 사용하긴하는듯)

### **Pros**

- Lightweight, open-source, and usable across all major cloud platforms and storage types.
- Flexible, format and framework agnostic, and easy to implement.

### **Cons**

- DVC version control is tightly **coupled with pipeline management**. This means if your team is already using another data pipeline tool, there will be **redundancy**. → 이거는 좀 문제가 되겠는데
- DVC is lightweight, which means your team might need to **manually develop extra features** to make it easy to use. → 이건 오히려 좋을것같은데

## Delta Lake

- ACID transactions(DB transaction의 안정성을 부여), data versioning, metadata management, and managing data versions.
- Data lake의 추상화된 계층이다 → data lake의 기능과 유사하다고 받아들이겠음

### **Pros**

- Offers many features that might not be included in your current data storage system, **such as ACID transactions or effective metadata management. → 꽤나 유용한 기능들 제공**
- Reduces the need for hands-on data version management and dealing with other data issues, allowing developers to focus on building products on top of their data lakes instead.

### **Cons**

- Delta Lake is often o**verkill for most projects** as it was developed to operate on Spark and on big data. → Spark or big data dependency
- Requires using a dedicated data format which means it is less flexible and not agnostic to your current formats. → **dedicated data format, 이건 좀 치명적인데.**
- Tool’s primary purpose is to **act more like a data abstraction layer**, which might not be what your team needs and can detour developers in need of a lighter solution. → tool 자체가 좀 무겁다는거잖아

## **Git LFS**

- 근본이지, extension of Git
- eliminate large files that may be added into your repository. (photo, ...)

### **Pros**

- **Integrates easily** into most companies' development workflows. → 역시 확정성, 유연함
- Utilizes the **same permissions as the Git repository** so there is no need for additional permission management. → permission 쉽다

### **Cons**

- Git LFS requires **dedicated servers for storing your data**. This, in turn, eventually leads to your data science teams being locked in as well as increased engineering work. → 이건 좋은거 아닌가? 유연하게 server 지정해서 쓸수있을거같은데
- Git LFS servers are not meant to scale, **unlike DVC**, which stores data into a more general easy-to-scale object storage like S3. → 아 지정한 서버만 써야된다고? 이럼 나가리지
- Very specific and may require using a number of other tools for other steps of the data science workflow.

## **Pachyderm**

- Pachyderm’s aim is to **create a platform** that makes it **easy to reproduce** the results of machine learning models by **managing the entire data workflow.**
- In this regard, Pachyderm is “the Docker of data.” → Docker와 밀접한 연관!?
- combination of both versioned data and Docker
    - 성학님, Docker compose로 구성하겠다 → 어쩌면 어울릴수도?

### **Pros**

- **Based on containers**, which makes your data environments **portable and easy to migrate to different cloud providers.**  → 이거 진짜 큰 장점인데
- **Robust and can scale** from relativity small to very large systems.

### **Cons**

- More of a **learning curve** due to so many moving parts, such as the Kubernetes server required to manage Pachyderm’s free version.
- With all the various technical components, it can be **difficult to integrate Pachyderm into a company’s existing infrastructure. → 허허...**

## **LakeFS**

- It provides a Git-like branching and version control model that is meant to work with your data lake, scaling to Petabytes of data. → 이게 상당히 맘에드는데
- Similar to Delta Lake, it provides **ACID compliance to your data lake**. However, L**akeFS supports both AWS S3 and Google Cloud Storage as backends**, which means it doesn't require using Spark to enjoy all the benefits. → 괜찮은데..?

### **Pros**

- Provides advanced capabilities such as A**CID transactions for easy-to-use cloud storage such as S3 and GCS, all while being format agnostic. → 이것만보면 훌륭한데?**
- **Scales easily, supporting very large data lakes. Capable of providing version control for both development and production environments.**

### **Cons**

- LakeFS is a **relatively new product**, so features and documentation might change more rapidly compared to other solutions. → 1년이 넘게 지났으니 괜찮지 않을까?
- **Focused on data versioning**, which means you will need to use a number of other tools for other steps of the data science workflow. → 오히려 좋아


## Reference
- https://dagshub.com/blog/data-version-control-tools/