# Warm-up Team Project </br> : Client/Server Programming using Web
## RFID project
   * Rasqberry pi와 사용할 수 있는 RFID를 사용하여, 일종의 본인 인증시스템 구현을 목적으로 한다.
     서랍, 캐비넷과 같이 본인이 아니면 열 수 없게하여 보안을 유지한다.
   * 또한 Key를 분실, 도난 당했을 경우를 생각해 열고 닫힌 이력을 확인할 수 있다.
##### RFID?
   * RFID(Radio-Frequency Identification)는 주파수를 이용해 ID를 식별하는 SYSTEM으로 일명 전자태그로 불린다. 
     RFID 기술이란 전파를 이용해 먼 거리에서 정보를 인식하는 기술을 말한다.

### 시스템 구성도
<img src="./Image/시스템구성도.PNG">

### 기능
  * 권한이 허락된 키가 아닐 경우
    * 문이 열리지 않으며(모터가 작동하지 않으며) 빨간불빛이 켜진다.
  * 권한이 허락된 키일 경우
    * 문이 열리며, 노란불빛이 켜진다.

### Web 구성도
  * 사용자 
    * http://ip/status : 잠금/열림 상태를 알 수 있다.
    * http://ip/log    : 잠그거나 열었던 기록을 확인 할 수 있다.
    
  * Server
    * http://ip/check  : RFID의 시리얼 넘버를 확인하여 권한이 있는지 확인한다.
    * http://ip        : 상태확인 및 기록을 DB로부터 가져오거나 DB에 기록한다
</br>
</br>
