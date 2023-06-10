import os,subprocess

elysium_truffle_json_paths = ["/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4Ea0Df261BA584572CDED3F2E35a0E63375Ac4f1/MyAdvancedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xEe045942b043B92cca0c454a553649EaA80873ea/TokenERC20.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xa46edd6a9a93feec36576ee5048146870ea2c3ae/EBU.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x8fd1e427396ddb511533cf9abdbebd0a7e08da35/TokenBank.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xe894d54dca59cb53fe9cbc5155093605c7068220/airDrop.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4a66ad0bca2d700f11e1f2fc2c106f7d3264504c/EBU.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x3f2ef511aa6e75231e4deafc7a3d2ecab3741de2/WhaleGiveaway2.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x89c1b3807d4c67df034fffb62f3509561218d30b/TownCrier.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x2972d548497286d18e92b5fa1f8f9139e5653fd2/demo.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x627fa62ccbb1c1b04ffaecd72a53e37fc0e17839/TokenBank.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7a4349a749e59a5736efb7826ee3496a2dfd5489/WhaleGiveaway1.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xf70d589d76eebdd7c12cc5eec99f8f6fa4233b9e/WhaleGiveaway2.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x958a8f594101d2c0485a52319f29b2647f2ebc06/Marriage.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xf2570186500a46986f3139f65afedc2afe4f445d/RealOldFuckMaker.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xdb1c55f6926e7d847ddf8678905ad871a68199d2/FreeEth.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb7c5c5aa4d42967efe906e1b66cb8df9cebf04f7/keepMyEther.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xbaa3de6504690efb064420d89e871c27065cdd52/VaultProxy.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xf29ebe930a539a60279ace72c707cba851a57707/B.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xec329ffc97d75fe03428ae155fc7793431487f63/TokenSender.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4b71ad9c1a84b9b643aa54fdd66e2dec96e8b152/airPort.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x19cf8481ea15427a98ba3cdd6d9e14690011ab10/daoPOLSKAtokens.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x78c2a1e91b52bca4130b6ed9edd9fbcfd4671c37/WhaleGiveaway1.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x610495793564aed0f9c7fc48dc4c7c9151d34fd6/SimpleWallet.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x663e4229142a27f00bafb5d087e1e730648314c3/PandaCore.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xa1fceeff3acc57d257b917e30c4df661401d6431/AirDropContract.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x3e013fc32a54c4c5b6991ba539dcd0ec4355c859/MultiplicatorX4.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x70f9eddb3931491aab1aeafbc1e7f1ca2a012db4/HomeyJar.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x524960d55174d912768678d8c606b4d50b79d7b1/Centra4.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x84d9ec85c9c568eb332b7226a8f826d897e0a4a8/WedIndex.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x39cfd754c85023648bf003bea2dd498c5612abfa/TokenBank.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x5aa88d2901c68fda244f1d0584400368d2c8e739/MultiplicatorX3.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x07f7ecb66d788ab01dc93b9b71a88401de7d0f2e/PoCGame.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xe09b1ab8111c2729a76f16de96bc86a7af837928/FiftyFlip.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xd5967fed03e85d1cce44cab284695b41bc675b5c/demo.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x3a0e9acd953ffc0dd18d63603488846a6b8b2b01/TokenBank.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xd2018bfaa266a9ec0a1a84b061640faa009def76/Pie.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x0cbe050f75bc8f8c2d6c0d249fea125fd6e1acc9/Caller.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7d09edb07d23acb532a82be3da5c17d9d85806b4/PoCGame.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb37f18af15bafb869a065b61fc83cfc44ed9cc27/SimpleWallet.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb620cee6b52f96f3c6b253e6eea556aa2d214a99/DrainMe.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xe4eabdca81e31d9acbc4af76b30f532b6ed7f3bf/Honey.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x52d2e0f9b01101a59b38a3d05c80b7618aeed984/EtherGet.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9d06cbafa865037a01d322d3f4222fa3e04e5488/Delta.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4051334adc52057aca763453820cb0e045076ef3/airdrop.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xe82f0742a71a02b9e9ffc142fdcb6eb1ed06fb87/Freebie.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x806a6bd219f162442d992bdc4ee6eba1f2c5a707/Pie.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb11b2fed6c9354f7aa2f658d3b4d7b31d8a13b77/DepositProxy.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xbebbfe5b549f5db6e6c78ca97cac19d1fb03082c/VaultProxy.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7b368c4e805c3870b6c49a3f1f49f69af8662cf3/W_WALLET.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x627fa62ccbb1c1b04ffaecd72a53e37fc0e17839/TokenBank.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xbe4041d55db380c5ae9d4a9b9703f1ed4e7e3888/MONEY_BOX.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xcead721ef5b11f1a7b530171aab69b16c5e66b6e/WALLET.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xf015c35649c82f5467c9c74b7f28ee67665aad68/MY_BANK.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x96edbe868531bd23a6c05e9d0c424ea64fb1b78b/PENNY_BY_PENNY.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7541b76cb60f4c60af330c208b0623b7f54bf615/U_BANK.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x93c32845fae42c83a70e5f06214c8433665c2ab5/X_WALLET.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x8505185D59CA2B1381A727C3429098C62B18E71a/NGToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x0b76544F6C413a555F309Bf76260d1E02377c02A/INT.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x687D9d6839817db4574AED33f45647109DFe9C2d/ChuCunLingAIGO.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x3501ECfa3f8b188915C72f36A93566585ba99336/CTest7.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x68E03D2DA62D026403C68601D650c877901876BF/ModiTokenERC20.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x584a0EC8A7A3fcfEd27Db5C234A9062863883778/GoodTimeCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xC1ca4E6FA2d888168a34a3429Bf186BcD9b475A0/HumanStandardToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x81d4703c5b3499B57397C999A72f492Fc681410D/CERB_Coin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7Dc4f41294697a7903C4027f6Ac528C5d14cd7eB/RemiCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9D5bd53fc23D6485A80B9879097E67a797365Ca5/Coffeecoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x531917942B6Bb866031aC22BB00E7838613753AC/TokenERC20.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x61dc161B06088b9cbaaD53391134929A83D1EB7A/MAVCash.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xFdB3c07c25F5a6879cC8b00685ed1A080c59615E/SpadeIco.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x95C9C35678C0B54008b1E3A2B0eA1730Fa7dBd06/GoodTo.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xaaabD58B6D94b21859F9Fc2B4E829f532283Cf69/UCoinToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x5aD6Dc0A267693c8A14AC9fF2A29c7D63A3d96c2/MP3Coin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x6Aac8CB9861E42bf8259F5AbDC6aE3Ae89909E11/BitcoinRed.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x5121E348e897dAEf1Eef23959Ab290e5557CF274/PolyAi.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xB5335e24d0aB29C190AB8C2B459238Da1153cEBA/Hexagon.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7D227Fe3C5885c3875180E03C548D09EBE1B0119/EncryptedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x3fe3D6f405b5858A320B33FbcB0Bea3b2C2eB7BE/MyToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9653cFd0865ad8313BEA2f0C2EC0584BFd05115B/FuturXe.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4b319cE02BdC8977Fb39fa70C49258a1a7C27d9B/UNLB.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xfdEA2AD97EC5297090c8d945f25a15f17f4C283d/FreeCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x824D83318d9637715a491B6CBb0244f55c0D5bAf/DYC.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xAc3Da587eac229C9896D919aBC235CA4Fd7f72c1/MyAdvancedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x42CEE7DD9B47C2ceE35ca996a712E8c99471d46f/ALUXToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9A7069c319E0052e071fcB437c8AA3343555dadC/AzurionToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xC1E2097d788d33701BA3Cc2773BF67155ec93FC4/IADOWR.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x05aAaA829Afa407D83315cDED1d45EB16025910c/SPXToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x219218f117DC9348b358b8471c55A073E5e0dA0b/GRX.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x6FC9c554C2363805673F18b3A2b1912cCE8Bfb8a/RocketCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7627de4B93263a6a7570b8dAfa64bae812e5c394/NexxusToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x3AC96Bbe8b60D715fD818B3FE242EdF9dEF20571/MyBoToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x27f706edde3aD952EF647Dd67E24e38CD0803DD6/UselessEthereumToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x63e634330A20150DbB61B15648bC73855d6CCF07/BlocklancerToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x0a9A9ce600D08BF9b76F49FA4e7b38A67EBEB1E6/GrowToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x81A9eBFDCd87cd291Eb5e5260901A898dF3bdafd/DaddyToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xc524079859fD32597F257c175c5f9E239C1Dd2DB/EncryptedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x524A1407223446e3BAb8819ABb3fb8348C29afEc/sumocoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x12480E24eb5bec1a9D4369CaB6a80caD3c0A377A/MyAdvancedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xB939C757bdFC75E28E1ae2b8c1a4640180B6087E/ReimburseToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x294eE9f35988aF1ce361409Cee4251a293D21f5c/MyAdvancedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x74fA9AA30b1b35c8F5bDB76F079C2624FC0b6498/MoxyOnePresale.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x30DdA19C0b94a88eD8784868Ec1e9375d9F0E27c/DSPXToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x47427A4921bdF2b3ac75eCF53193A5265aF4a12F/WMCToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x7241d179d92E86237bB460f8A19FAE369a8846a3/CGCToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x332124F226e80c3AFdBb59271f550881b20604A1/PlazaToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x0bb217E40F8a5Cb79Adf04E1aAb60E5abd0dfC1e/SwftCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xA1f87895550EAc6a8e9E4318466F482612a5986D/GZSToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xe649E289bc2A29E3C7bEEBD187BA3ee2B0cDC759/JiucaiToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb75a5e36cC668bC8Fe468e8f272Cd4a0fd0fd773/Token.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xE2E6D4BE086c6938B53B22144855eef674281639/LinkToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x50ca2DE80e803bF4b00f188545BCA959540C5582/SpadePreSale.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9107C1B28d775E59f98BF3f4dE3b959816CF5526/MyAdvancedToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x30ceCB5461A449A90081F5a5F55db4e048397BAB/Tracto.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb57E2EC276460a993393cA1bB2BdAe6c8170c73A/CTB.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x1C65557B72804569BcD25cE53575A9C712e2Eff5/Play2LivePromo.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4dAA9DC438a77Bd59E8A43C6D46cbfE84cD04255/BattleToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x78B7FADA55A64dD895D8c8c35779DD8b67fA8a05/ATL.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xDe39E5E5a1B0eEB3Afe717D6d011CaE88D19451e/DimonCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x4D391B4350cA1C690eBaf00d35bfcDd5721470F8/Betcash.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xc6689EB9a6D724B8D7B1d923fFd65B7005dA1b62/SEC.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x2d6669c810bf1444D2e5e7f4cfC56a4c10cf7A2A/HYIPToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9f03d94bf3545153cb28014bC7D1e7177cA99034/MyYLCToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xDf07Fa1b102c00124E96F18Ea612bbbe553f50e1/YiTongCoin.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x9B13F5260219282464893DBeaDb65000d75E8263/GFCB.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x0661F731f7f442A4147b87aF5e77a9ECC7ed744E/ETY.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x10E886BAcD4A12C21Bb39646751374Eae495B776/Krown.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xb57bB80bc676Bc1134432860bd27A9D048ABe0B0/Goutex.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xF94d0b334b2CDEaAFCd7B2796B8743fb72dbFFF1/Jitech.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0xFf1560afEF58be59b11C72734ad1d89db63e4E71/ExtremeToken.json",
"/bdata2/gcf/tosemr1/Elysium/PVD_truffle_json/0x8EEb73BEFd9285d686d6Cf7649Ed657514a714CB/MalaysianCoin.json"]

elysium_truffle_json_paths_scrd = [
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0xc7d020d8C92D099B3ADE17321310b4815eF20A90/AirDrop.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x169e59a41BA10600Fddd1b0A72921f503b31D96B/IcoOKOToken.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x6994699c731dd7e389C209201eC51e8aff283bF9/tokensale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x87bE69E5C196E0309CDF6957FD7141FDA1DF2B97/SaleExtendedBCO.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x0a630de26e5B41eaef08741e74da4018A6C2E14c/dgame.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x92033Cc5D60dE8fC01e7d4125713e05194989e1e/HodboCrowdsale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x53CE47cbe7F2be0AEcD086a70182A98c907D024d/EasyMineIco.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0xc8986Ecd41Fb420268f1f4285931379357c4142B/YobCoinCrowdsale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0xCB58A0bDdb9c972D1020d3F9e94C3401960A12d8/Crowdsale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x0961375ed779Fe16435D5D430Da00A5bAC527e46/Presale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x6A57883B5748Bf3631aC2E0d43BF0D6f6cBCD16b/LescoinPreSale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x6459fe2c8d7c26C0011772310D8cA0f570F1D667/ClassyCoinAirdrop.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0xE07E687DC4b244D574F37490948C7f4aa921D958/ApplauseCashCrowdsale.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x5027880b5A4C5BBB88D229a334Aa8F31e6e67197/HDLContract.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0x79A198b2355CA2aef695d8a4987582E093911EBb/SiringClockAuction.json",
"/bdata2/gcf/tosemr1/Elysium/SCRD_truffle_json/0xD113244B9049943D4bc6fEf3048d24EDf92dd788/Issuer.json"]
address_contractname=dict()
address_jsonpath = dict()
address_lower = dict()
for json_path in elysium_truffle_json_paths_scrd:
    json_path_split = json_path.split("/")
    address_contractname[json_path_split[-2]]=str(json_path_split[-1])[:-5] # address: contract name
    address_jsonpath[json_path_split[-2]] = json_path # address: truffle json path
    address_lower[str(json_path_split[-2]).lower()] = json_path_split[-2] # address lowercase : address in SCRD

# print(elysium_fixed_contracts)

truffle_path = "/home/yjj/mydir/truffle_example/elysium/"

for dir in os.listdir(truffle_path):
    if str(dir).lower() not in address_lower.keys(): 
        # subprocess.run("rm -r {0}".format(dir),shell=True,cwd=truffle_path)
        continue
    else:
        contract_path = os.path.join(truffle_path,dir)
        subprocess.run("rm ./build/contracts/*",shell=True,cwd=contract_path)
        subprocess.run("cp {0} ./build/contracts/".format(address_jsonpath[address_lower[str(dir).lower()]]),shell=True,cwd=contract_path)
        subprocess.run("rm ./contracts/*",shell=True,cwd=contract_path)
        subprocess.run("rm result*",shell=True,cwd=contract_path)

        file_data = ""
        #/home/yjj/mydir/truffle_example/elysium/0xec329ffc97d75fe03428ae155fc7793431487f63/migrations/1_deploy_contract.js
        with open(os.path.join(contract_path,"migrations/1_deploy_contract.js"), "r", encoding="utf-8") as f:
            file_data += "const json = require(\"{0}{1}/build/contracts/{2}.json\"); \n".format("/workdir/truffle_example/elysium/",dir,address_contractname[address_lower[str(dir).lower()]])
            file_data += "const contract = require('@truffle/contract'); \n"
            file_data += "const {0} = contract(json); \n".format(address_contractname[address_lower[str(dir).lower()]])
            file_data += "{}.setProvider(this.web3._provider); \n".format(address_contractname[address_lower[str(dir).lower()]])

            num = 1
            for line in f:
                if num == 1: 
                    num += 1
                    continue
                elif "deployer.deploy" in line:
                    file_data += str(line)[:-2]+", {from: accounts[0]})\n"
                else:
                    file_data += line
        with open(os.path.join(contract_path,"migrations/1_deploy_contract.js"),"w",encoding="utf-8") as f:
            f.write(file_data)

        file_data = ""
        with open(os.path.join(contract_path,"run.sh"), "r", encoding="utf-8") as f:
            file_data = f.read()
            file_data = file_data.replace("truffle compile","")
            file_data = file_data.replace("truffle migrate --network develop","truffle migrate --network develop > result_deploy.txt 2>&1")
        with open(os.path.join(contract_path,"run.sh"), "w", encoding="utf-8") as f:
            f.write(file_data)

