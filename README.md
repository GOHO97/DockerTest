# Eazel_datahunting_<윤경호> 
  
검색 결과는 google custom search API를 이용하였습니다.  
최종 결과물의 파일명은 gsrSortByDate.tsv이며 정렬 방식은 날짜 오름차순입니다.  
  
### 최대 페이지 셋팅  
전역 변수 setPage에 1 ~ 10 범위의 정수를 할당해주시면 됩니다. 
  
### 도커파일 빌드 하는법 
docker build -t 이미지명 .
  
### 도커 이미지 실행하는법
docker run -d -p 80:80 --name 컨테이너명 이미지명:latest
  
### 요청 주소(GET) 
host서버의 IP:80 으로 접속 하시면 됩니다.  
hostIP:80/search?keyword=키워드입력
