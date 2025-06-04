from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()

model1=ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', temperature=0)

model2=ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', temperature=0)

prompt1= PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2= PromptTemplate(
    template="Generate 5 short questions from the following text \n {text}",
    input_variables=['text']
)

prompt3= PromptTemplate(
    template="Merger the provided notes and quiz into single document \n notes-> {notes}, quiz-> {quiz}",
    input_variables=['notes', 'quiz']
)

parser= StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'notes': prompt1| model1 | parser,
        'quiz': prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model1 | parser 

chain= parallel_chain | merge_chain

text=""" The Internet of Things refers [2] to ubiquitous end devices and facilities, including sensors with “intrinsic
 intelligence”, mobile terminals, industrial systems, building control systems, home intelligence devices, video
 surveillance systems, etc., and externally enabled, such as RFID-attached assets, individuals and vehicles carrying
 wireless terminals, etc. “smart parts or animals” or “smart dust” through a variety of wireless and / or wired long
 distance and / or short-range communication networks to achieve interoperability (M2M), application integration
 (Grand Integration / MAI), and cloud-based SaaS operations and other modes, intranet (Intranet), private network
 (Extranet), and / or the Internet (Internet) environment, using appropriate information security mechanisms[2] to
 provide secure, controllable and even personalized real-time online monitoring, location and traceability, alarm
 linkage, dispatching command, plan management, remote control, security, remote maintenance, online upgrade,
 management and service functions such as statistical reports, decision support, and leadership of the desktop
 (Cockpit Dashboard), to achieve “all things, high efficiency, energy saving, safety, environmental protection,
 control, camp” integration TaaS service.
 Smart home [4],[5] is a versatile system includes visual intercom, home security, remote monitoring of home
 appliances, remote video surveillance, telemedicine diagnostics and care systems, online education systems, and
 home movie star systems. The advent of the concept of the internet of things has broken the traditional thinking of
 the past. The idea in the past has been to separate the physical infrastructure from the IT infrastructure, on the one
 hand, airports, roads, buildings, and on the other hand, data centers, personal computers, broadband, and so on. In
 the era of the internet of things, reinforced concrete and cables will be integrated into chips and broadband as a
 unified infrastructure.
 With the wide application of electronic technology in real life, people and more and more aware of the
 convenience brought by electronic products to life, especially in the 1980s, the emergence of smart home provides
 and more enjoyable life for people broad platform. Although smart home development has been around for 30 years,
 smart products are still the mainstream of today’s development, especially the emergence of the internet of things,
 and further promote its development. Therefore, this design research on smart home products is in line with the
 trend of the world, and makes itself into the industry of smart home product development, so this product research
 and development has great research significance. With the NB-IOT standard freeze in June this year, the foundation
 of the large-scale commercialization of the recently-recognized NB-IOT has finally been implemented. It is widely
 believed that 2017 will be the first year of commercial use of the NB-IOT network. As a low-power WAN
 technology promoted by Huawei and many operators, NB-IOT received extensive attention in the industry since its
 launch. The topic of LoRa and NB-IOT has not been interrupted. One of the NB-IOT Alliance members of Vodafon,
 one of its executives even publicly stated that “NB-IOT will lead to LoRa’s demise”.
 2. Related work and methodologies used
 2.1. System design
 According to the design requirements and functions, the system includes gateway board, a node board, a PC, and
 Android phone. The main control MCU of the nuclear gateway board adopts the LPC1769 chip, the BN-iot module
 adopts the xbee module, the wifi module adopts the wifibee module, the main control chip of the NB-iot node
 adopts the LPC1114 chip, and the temperature and humidity sensor adopts the DHT11 sensor. The working
 framework of the system’s overall module is shown in Figure 1.
6 
Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13
 ChanthaphoneSisavathetal./ProcediaComputerScience00(2020)000–000 3
 Fig.1.Theframeworkoftheoverallsystemmodule
  Xbeemodule:ThexbeeS2moduefromDigiisashort-range, low-powerdatatransmissionsmodulewitha
 2.4GHzband,built-inNB-iotprotocolstack,andallperipheralcircuitsthroughtheconfigurationsoftwareX
CTUonthePC.Configurethemoduletotransmitpowerchannelandothernetworktopologyparameter.The
 NB-iotcoordinatorisanxbeemoduleintegratedontheembeddedgatewayboardthatconnectstotheMCU
 throughaserialport.Afterthenetworkingofthexbeemoduleissuccessful,thereceiveddataisoutputthrough
 itsport,andthetransmitteddataisinputthroughitsserialport.
  Wifibeemoule:Thewifibeemoduleinducesan802.11b/gwirelesstransmitter,a32-bitprocessor,aTCP/IP
 stack,areal-timeclock,apowermanagementunit,andananalogsensorinterface.Thismoduleisper-installed
 withRovingfirmware.Toincreaseitsintegrationtoreducethedevelopmenttimeofapplicationsthatiscriticalto
 theuser.Inthesimplestandmostpracticalsetup, thehardwareonlyneedsfourconnections(power, tx,rxground)
 tocreateaWirelessdataconnection.ThewifibeemoduleiswidelyusedintheUnitedStates,Canada,Australia,
 IsraelandEurope.EstablishingRFcommunicationdoesnotrequireanyadditionalconfigurationandthe
 module’sdefaultconfigurationsupportsawidevarietyofDeviceapplication.Youcanalsousethecommandto
 configurethemoduletoperformsomespecialfunctionthatyouhavecustomized.Whenthewifibeemodule
 receivesdata,itoutputsthroughitsserialport,andwhenitsendsdatathroughitsserialport.
  NB-iotNodeBoard:theBN-iotgussetplateofthisexperimentwasalaboratoryboard.TheNB-iotnodeboardis
 composedofLPC1114chip,FT232RLchip,DHT11senserandxbeemodel.TheLPC1114isthecoreofthe
 entirenodeboard.FT232RLisinterfaceconversionchipthatconvertUSBtoserialUARTinterface.DHT11isa
 temperatureandhumiditysensorthecollectstemperatureandhumiditydata.Thexbeemoduleisresponsiblefor
 connectingtotheNB-iotnetwork.
 2.2.Overviewofthedesignofthegatewayboard
 ThegatewayboardismainlycomposedofLPC1769maincontrolchip,W25Q18FVchip,xbeemodulewifibee
 module.LPC1769istheheartofthewholesystem.TheresponsibilityofW25Q18FVchipistostorewebpagedata,
 xbeemodule establishes NB-iot network, wifibeemodule is responsible for communicationwithAPP. The
 peripheralstructureofthegatewayboardisshowninFigure2
4
 Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13 
7
 Chanthaphone Sisavath et al. / Procedia Computer Science 00 (2020) 000–000
 Fig. 2. Gateway board peripheral structure
 The LPC1700 series AMR is a second-generation ARM cortex-M3 core-based micro-controller from NXP. It is a
 high-performance, low-power 32bit microprocessor designed for embedded system applications with an operating
 frequency of up to 120MHz. A 3-stage pipeline and Harvard architecture with independent local instructions and
 data structures and a low-performance third bus for peripherals, enabling code execution speeds of up to 1.25
 MIPS/MHz and including an internal that supports random jumps Prefects unit. The LPC1700 series ARM adds a
 dedicated flash memory acceleration module, which enables the running code in Flash to achieve better performance.
 It is suitable for instrumentation, industrial communication, motor control, lighting control, alarm system and other
 fields [25].
 The peripheral components of the LPC1700 series Cortex-M3 micro-controller include up to 512KB of flash
 memory, 64KB of data memory, Ethernet MAC, USB master/slave/OTG interface, 8-channel general purpose DMA
 controller, 4 UARTs, 2 CAN channel, 2 SSP controllers, SPI interface, 3 I2C interfaces, 2-input and 2-output I2S
 interfaces, 8-channel 12-bit ADC, 10-bit DAC, motor control PWM, quadrature encoder interface, Four general
purpose timers, a 6-output general-purpose PWM, an ultra-low-power RTC with independent battery power, and up
 to 70 general-purpose I/O pins [9].
 This design mainly uses the Ethernet peripheral functions of the LPC1769.The Ethernet module contains a full
featured 10Mbps or 100Mbps Ethernet MAC (Media Access Controller) that optimizes its performance by using
 DMAhardware acceleration. The Ethernet module has a large set of control registers that provide: half-duplex/full
duplex operation, flow control, control frames, retransmission hardware acceleration, receive packet filtering, and
 wake-up on the LAN. The automatic frame transmission and reception operations using the Scatter-Gather DMA
 alleviate the CPU workload. The Ethernet module is an AHB host that drives the AHB bus matrix. Through the
 matrix, it can access all the ram memory on the chip. It is recommended that Ethernet use ram exclusively by using
 one of the ram modules to handle Ethernet communications. Then the module can only be accessed by Ethernet and
 CPU, perhaps GPDMA, to get the maximum bandwidth of the Ethernet function. The Ethernet module uses the
 SMII (Simplified Media Independent Interface) protocol and the on-chip MIIM (Media Independent Interface
 Management) serial bus, as well as MDIO (Manage Data Input/Output) to interface with the off-chip Ethernet PHY.
 2.3. Overview of uC/OS Operating system and uIP Protocol
 The uC/OS-II is μC/OS, it is a portable, implantable ROM, droppable, pre-emptive, real-time multitasking
 operating system kernel. It is widely used in microprocessors, microcontrollers and digital signal processors. The
 μC/OS and uC/OS-II are designed for embedded applications in computers, and most of the code is written in C.
 The CPU-related parts of the CPU are written in assembly language, and the assembly language part of a total of
 about 200 lines is compressed to a minimum in order to facilitate porting to any other CPU. Users can embed
 uC/OS-II into the developed product as long as they have a standard ANSI C cross compiler and software tools such
 as assembler and connector. The uC/OS-II features high execution efficiency, small footprint and excellent real-time
 performance and scalability. The smallest kernel can be compiled to 2KB.uC/OS-II has been ported to almost all
 well-known CPUs.
 Strictly speaking, uC/OS-II is just a real-time operating system kernel it only such as task scheduling, task
8 
Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13
 ChanthaphoneSisavathetal./ProcediaComputerScience00(2020)000–000
 management, timemanagement,memorymanagement, communication and synchronization between tasks. No
 additionalservicessuchas inputandoutputmanagement, filesystem,network,etc.areprovided.However,dueto
 thegoodscalabilityandopensourceofuC/OS-II, thesenon-essential functionscanbecompletelyimplementedby
 usersthemselvesaccordingtotheirneeds.TheuC/OS-IIgoal istoimplementapre-emptivereal-timekernelbased
 onpriorityschedulingandprovidethemostbasicsystemservicessuchassemaphores,mailboxes,messagequeues,
 memorymanagement, andinterruptmanagement.TheuC/OS-II isdesignedwithonlyoneCPUinthesystem. In
 suchasystem,onlyonetaskataspecificmomentwilloccupytheCPU,whileothertaskscanonlybeinotherstates.
 The tasks inuC/OS-IIhave fivestates: sleepstate, readystate, runningstate,waitingstate, and interrupt service
 status [6].Under systemmanagement, a task canbe transformed between five different states. The conversion
 relationshipisshowninFigure3.
 Fig.3.TaskstatuesswitchingofuC/OS-II
 TheuC/OS-II is releasedas sourcecode, but it doesnotmean it isopensourcesoftware.Youcanuse it for
 teachingandpeaceful research;but ifyouuse it forcommercialpurposes, youmustobtainacommercial license
 throughMiriam.
 uIPisaverysmallTCP/IPprotocol stackdesignedspecificallyfor8-bit and16-bitmicrocontrollers. uIPis
 writtenentirely inCandcanbe easilyported toavarietyof different architectures andoperating systems.A
 compiledstackcanruninafewkilobytesofROMorhundredsofbytesofRAM.Andthehardwareprocessinglayer,
 theprotocolstacklayerandtheapplicationlayershareaglobalbufferarea,andthereisnocopyof thedata,which
 greatlysaves space and time.Due to its simple structure and reliable function,many8-bitmicrocontrollers are
 portedtotheuIPprotocolstack[1].TheuIPprotocol stackremoves thefunctions that arenotcommonlyusedin
 TCP/IP, simplifies the communication process, but retains the protocols that must be used for network
 communication. The design focuses on the network layer and transmissionof IP/TCP/ICMP/UDP/ARP. Layer
 protocolensurestheversatilityandstructuralstabilityofthecode.
 3.Experimentandresults
 3.1.Customizationofcommunicationprotocols
 Sincexbeeandwifibeeareconfiguredtocommunicateintransparentmode, inordertofacilitatedataprocessing
 andsecondarydevelopment, thedesigncustomizesatransportprotocolbetweenxbeecommunicationandwifibee
 communicationwithAPP.TheformatofitstransportprotocolisshowninTable1.
 Table1.ProtocolPacketFormat
 HeadFlag PacketLength CommondId CommondPara CRC RearFlag
 1Byte 1Byte 1Byte nByte 1Byte 1Byte
 0X7E LEN CmdID
 0X00
 ~
 0XFF
 …
 0X00
 ~
 0XFF
 0X00
 ~
 0XFF
 0X7E
 Table2isadescriptionoftheprotocolinTable1.TheprotocoldescriptionisshowninTable2
6
 Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13 
9
 Chanthaphone Sisavath et al. / Procedia Computer Science 00 (2020) 000–000
 Table 2. Protocol Description
 Head Flag
 Packet header, fixed to 0x7E
 Packet Length
 The entire packet length, 1 byte in length, contains all bytes from HeadFlag~RearFlag
 CommondId
 instruction.
 CommondPara
 Instruction parameters.
 CRC
 The CRCcheck, the value of the CRC is the sum of the PacketLength value plus the Commond Id
 value.If CRC=PacketLength+Commond Id, then OK, otherwise, the verification fails.
 Rear Flag
 End of packet, fixed at 0x7E
 Since the system needs to transmit data content temperature and humidity data and control the semaphore of the
 LEDswitch, Commond Id defines two instructions, as described in Table 3.
 Table 3. Instruction Description
 Command
 CommandId
 CommondPara
 ParaLength ParaData0
 ParaData1 ParaData2 …
 Temperature and humidity 0x01
 0x07
 temperature
 humidity
 invalid
 invalid
 light
 0x02
 0x06
 0x01 or
 0x00
 invalid
 invalid
 invalid
 To be determined
 To be determined
 As shown in Table 3, when Command Id is 0x01, only the first two data are valid for the Commond Para
 parameter, which are temperature data and humidity data. When Command Id is 0x02, only the first data is valid for
 the Commond Para parameter. ParaData0 is 0x01 for the light-on action, and ParaData0 is 0x00 for the light-off
 action.
 3.2. Implementation of xbee communication
 The xbee module can be configured through the X-CTU host software. The X-CTU host computer interface is
 shown in Figure 4.
 Fig. 4. X-CTU interface
10 
Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13
 ChanthaphoneSisavathetal./ProcediaComputerScience00(2020)000–000
 Thexbeenetworkingconditionmust haveamoduleconfiguredas acoordinator, so thexbeemoduleon the
 gatewayboardisconfiguredasacoordinator throughX-CTU,andthexbeemoduleofthenodeboardisconfigured
 asaterminalthroughX-CTU.Onceconfigured,thexbeemodulescancommunicatewitheachother.
 3.3.Implementationofwifibeecommunication
 This design needs to configure thewifibeemodule as awifi service hotspot for theAPP to connect and
 communicatewiththeAPP.Wifibee'sconfigurationtoolcanbeimplementedonlywithaserialportassistant.Inthe
 serialportassistant,enterthecommandcodeinturn:
 1. setwlanjoin7
 2. setipdhcp4
 3. setipaddress192.168.190.1
 4. setipgateway192.168.190.1
 5. setipnetmask255.255.255.0
 6. setipremote2000
 7. save
 8. Reboot
 Through the above command configuration, wifibee is configured as awifi hotspotwith an IPaddress of
 192.168.190.1andaportnumberof2000.
 3.4.Appimplementationprocess
 Themain functionof the app is todisplay the temperature andhumiditydata informationcollectedby the
 gatewayboardandtocontrol thestateof theLEDLight switch.Thisdesignapponlycontainsone interface.The
 interfacemainlycontains fivefunctioncontrols, namelythreeButtonsandtwoTextViews.The threeButtonsare
 respectivelydefinedasconnectingwifibeeaction, lightingthenodeboardLEDlightaction,andturningoffthenode
 boardLEDlight action, and their idsaredefinedasStartConnect, SendLON, andSendLOFF, respectively. The
 functionof thetwoTextViews istodisplaythetemperaturevalueandthehumidityvalue,andtheir idsaredefined
 astxt_tempandtxt_humidity,respectively.
 TheAPPmustbeconnectedtowifibeetorunitsfunction.ThecontrolidisStartConnect isboundtolistenforthe
 StartClickListener event, and its event mainly performs the action of connecting wifibee. When the
 StartClickListenereventoccurs,sinceisConnectingisinitializedtofalse, thesystemcreatesathreadthat listensto
 theserver.Sincewifibeehasbeenset toIP192.168.190.1, theport is2000wifihotspot.SodefineStringmsgText
 ="192.168.190.1:2000"asthetargetof thelisteningserver.WhentheAPPsuccessfullyconnectstowifibee, itstarts
 toenterthelisteningstate,anditsButtonwilldisplaythe“connected”state.TheidofthecontrolButtonisboundto
 listen to theSendLightOnevent, and itseventmainlyperforms theactionof lighting theLEDlight of thenode
 board.
 WhentheSendLightOneventoccurs, firstdefineanarraytobesent, iecharsendlighton[]={0x7e,0x06,0x02,
 0x01,0x08,0x7e}, thedatainthearrayconformstotheprotocolestablishedbythisdesign.WhentheSendLightOn
 eventoccurs, ifthesystemisproperlyconnectedtotheserver, theAPPwill light theLEDlightdatatothegateway
 board.Ifthesystemisnotproperlyconnectedtotheserver, theAPPinterfacewillprompt"Noconnection."
 Thecontrol id's idisSendLOFFisboundtolistenfor theSendLightOFFevent,anditseventmainlyperforms
 theactionofturningoffthenodeboardLEDlight.Thebindingcodeandeventcodearethesameasthecontrolidof
 thecontrolbutton.Theonlydifferenceisthat theSendLightOFFeventdefinesthedatasent tothegatewayboardas
 thedatafortheturn-offlight,iecharsendlightoff[]={0x7e,0x06,0x02,0x00,0x08,0x7e}
8
 Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13 
11
 Chanthaphone Sisavath et al. / Procedia Computer Science 00 (2020) 000–000
 3.5. PC access gateway board test
 After configuring the correct setting of the PC network adapter, open the browser and enter 192.168.150.200 to
 access the gateway board is shown in Figure 5.
 Fig. 5. Login interface
 In the figure enter the user name and password to enter the corresponding page. The initial user name is: Senwei
 and the password is: 123456. Enter the user name and password correctly, the PC will first login to the home page
 interface, the home page interface shown in the PC browser can click the home page, the monitoring canter, control,
 and send us a request to the server through is navigation bar it shown the monitoring centre interface.
 Fig. 6. Home Screen
 As shown in Figure 6 due to the limitations of the xbee module and the sensor, the monitoring centre of this design
 only has the temperature, humidity and light status of the hall as valid data, and other data are analogy data. The
 temperature value and humidity value shown in Figure 6 are the temperature and humidity data collected by the gusset
 board. When the light status is ON, it means that the LED Light of the gusset plate is on. If the light status is OFF, it
 means this time. The LED Light of the gusset is off. The control centre interface is an additional requirement for this
 graduation project. Therefore, due to limited time, only the opening and closing buttons of the electric light are valid
 values
 in the control centre, and other buttons are invalid. When the button of the light is turned on, the Led light of
 the node board will be lit, and a request of the monitoring centre will occur in the PC browser to display the state of the
 Led light of the node board when the button of the light is turned off, the LED Light of the node board will be
 extinguished, and a request of the monitoring centre will occur in the PC browser to display the status of the Led light of
12 
Chanthaphone Sisavath  et al. / Procedia Computer Science 183 (2021) 4–13
 ChanthaphoneSisavathetal./ProcediaComputerScience00(2020)000–000
 thenodeboard
 3.6.Mobileappaccessgatewayboardtes
 MobilephoneAmust connect to thewifibeehotspot in the setupcenter to implement theAPPandwifibee
 communicationfunction.wifibeehasbeenconfiguredasawifihotspotnamedSANFI,sothemobileAPPshouldbe
 connectedwithwifibee.Forcommunication,youmustconnect tothewifihotspotnamedSANFI inthephonewifi
 settings.WhenthemobileAPPisconnectedtothewifihotspot,opentheAPPandclickthe“StartConnect”button,
 theAPPwill enter the listeningstate, and the“StartConnect button”will switch to the“Connected” state.And
 displaythe temperatureandhumiditydatasentbythegatewayboardinreal time.APPinterfaceis inthelistening
 stateinterface
 4.Conclusionandfutureworks
 ThesmarthomebasedontheInternetofThingsdoesnotonlyincludetheapplicationofembeddedtechnology,
 but alsoacomplexandcomprehensiveproject.Whiledoingresearchonembeddedsystems,wehave toconsider
 other issues such as network, environmental protection, and ecology froma systemperspective. Alot of the
 knowledge involved is far frommyprofessional knowledge, such as architecture, home appliances, etc.,more
 involvedinalotofhumancontent.Thearchitectureofthesmarthomeandcampusdescribedinthispaperisbased
 on thecurrent advancedsoftwareandhardware technologies, but it hasnot completelyescaped the shacklesof
 traditionalconcepts.Thedesignofsmarthomesmustbeforward-lookingandcloselyfocusoncurrent technology
 developments toensure that thestructurebeingdesigned, the technologyusedarescalableandhavea longer life
 cycle.Thesystemstructureproposedinthispaper introducesmoreadvancedsoftwareandhardware technologies
 anddeterminesthedirectionforfurtherresearch.
 In2014,GoogleacquiredthesmarthomecompanyNest,whichcausedpeople inthe industrytotalkabout the
 developmentofsmarthomes.Indeed,withtherapiddevelopmentofthesocialandeconomiclevel, thepaceoflifehas
 accelerated,makingpeoplemorecomfortablewiththecomfort, safetyandintelligenceof familylife.Therefore, the
 developmentofsmarthomemustbeoneofthebiggestmainstreamsinthe21stcentury.Thisgraduationdesignproduct
 isinlinewiththetrendof thetimes.TheIOTisusedtobuildasmarthomegatewaysystem.Althoughthefunctions
 realizedby thisdesignare relativelysimple, thesystemreservesmany interfaces for extending functions, suchas
 refrigeratorsandair conditioners.Control, so there is still a lotof roomfordevelopment in thisgraduationdesign
 product.Andthisproducthasaddedtheappterminal,whichmakesthewholesystemmoreperfect.Theoperationof
 theappmakestheusermoreconvenienttouse.Therefore,theupgradeoftheappisalsothetoppriorityofthisdesign


"""
result=chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()