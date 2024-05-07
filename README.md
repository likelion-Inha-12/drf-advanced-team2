# drf-advanced-team2

drf실습 2팀 과제 레포입니다.
### 1. 과제를 생성합니다.
-특정 과제를 생성합니다
  ![](./images/api_1.png)
### 2. 특정 과제에 대한 제출물을 생성할 수 있습니다.
-과제의 id를 받아온 후 해당과제에 대한 제출물을 생성합니다
  ![](./images/api_2.png)

### 3. 생성되어 있는 전체 과제들의 목록을 조회할 수 있습니다. 
- 그동안 만들었던 category 및 과제들의 목록을 return합니다
  ![](./images/api_3.png)

# ERD

![](./images/DBD.png)

- 과제:카테고리를 N:1 관계로 설정했습니다.
- 과제:제출물을 1:N 관계로 설정했습니다.

# API 명세서

마지막에 넣을게요

# API 한 줄 설명 + postman 스크린샷

### 4. 특정 과제 조회 api

- path parameter로 조회하고자 하는 과제의 id를 받아와서, 해당 과제와 제출물들의 정보까지 return합니다.
  ![](./images/api_4.png)

### 7. 파트별 과제 조회 api

- query string으로 조회하고자 하는 파티를 받아와서, 해당하는 과제들의 제목, 생성 일자, 파트를 return합니다.
  ![](./images/api_7_1.png)
  ![](./images/api_7_2.png)
  ![](./images/api_7_3.png)

### 8. 카테고리별 과제 조회 api

- query string으로 조회하고자 하는 카테고리를 받아와서, 해당하는 과제들의 제목을 return합니다.

  ![](./images/api_8.png)
