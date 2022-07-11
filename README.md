# 📌 가상화 DB 로그 자동 기록 프로그램
* (보안 관계로 본 프로그래머가 개인적으로 나중에 재구성한 프로그램임을 알립니다.)

## 💁‍♂️ 회사 요구 사항

*  파이썬을 이용, exe 프로그램으로 만들어 줄 것
*  MS SQL을 써서 DB를 구성할 것
* 가상화를 담당하는 프로그램이 설정한 시간에 자동으로 작동 할 것
* 해당 로그를 DB 및 엑셀 파일로 저장할 것
* 정보가 외부로 노출 되지 않을 것
* OTP기능을 넣어 줄 것 
* 3년 분량의 정보가 기록 되어야 함
* 해당 OS는 WindoW에서 작동 해야 할 것

## ✍️ Idea 및 해결 방안

* 프로그램의 관리를 효율적으로 하기 위해 Setting을 담당하는 프로그램과 실질적으로 프로그램이 돌아가는 부분을 분리해서 만듬
* 정보 보호를 위해 기록되는 모든 정보는 복호화
* 설정한 시간에 자동으로 동작 하기 위해서 window 언어를 사용 
* 대량의 데이터를 관리 하기 위해서 DB 테이블 생성시 년도를 통한 파티션 기능 추가

## 💁‍♂️ Detail Role
* 홍한표 책임 엔지니어 
  * 가상화 엔지니어 팀장님
  * 엔지니어들 기능 요구사항 정리해서 프로그래머와 소통
  * citrix를 통한 가상화 개념 설명 
  * 가상 window 환경 구현 및 세팅 담당 

* 김병석 선임 프로그래머
  * 엔지니어와 소통해서 프로그래머 환경 설정
  * DB 구성 및 업데이트
  * 기능 추천 
  * 프로그램 UI 디자인
  * 프로그램 핵심 기능 구현

## Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>

## Technologies
<img src="https://img.shields.io/badge/git-red?style=flat-square&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/Microsoft SQL Server-blue?style=flat-square&logo=Microsoft SQL Server&logoColor=white"/> <img src="https://img.shields.io/badge/Windows System language-orange?style=flat-square&logo=Windows&logoColor=white"/>
