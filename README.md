# Ubuntu(Virtual Box)에서의 Docker file(fast API Server) 빌드 및 이미지 실행
  
![Resized_1669268249026](https://user-images.githubusercontent.com/101491213/203704838-2f44b863-d472-444c-9986-ec0cb39f65e2.jpg)
  
![Resized_1669268250469](https://user-images.githubusercontent.com/101491213/203704898-646e8277-4f07-490d-908a-cf66e92eb993.jpg)
  
검색 결과는 google custom search API를 이용하였습니다.  
최종 결과물은 root 디렉토리로 저장 되며 파일명은 gsrSortByDate.tsv입니다.  
정렬 방식은 날짜 오름차순입니다.  
  
### 최대 페이지 셋팅  
전역 변수 setPage에 1 ~ 10 범위의 정수를 할당해주시면 됩니다. 
  
### 도커파일 빌드 하는법 
docker build -t 이미지명 .
  
### 도커 이미지 실행하는법
docker run -d -p 80:80 --name 컨테이너명 이미지명:latest
  
### 요청 주소(GET) 
host서버의 IP:80 으로 접속 하시면 됩니다.  
hostIP:80/search?keyword=키워드입력
