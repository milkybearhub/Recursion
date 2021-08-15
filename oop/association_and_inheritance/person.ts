import { Wallet } from './wallet';

class Person {
  constructor(
    public firstName: string,
    public lastName: string,
    public age: number,
    public heigtM: number,
    public weightKg: number,
    public wallet: Wallet
  ){
    this.firstName = firstName
    this.lastName = lastName
    this.age = age
    this.heigtM = heigtM
    this.weightKg = weightKg
    this.wallet = wallet
  }

  getCash() {
    if (this.wallet == null) { return 0 }
    return this.wallet.getTotalMoney()
  }

  printState() {
    console.log('firstname - ' + this.firstName)
    console.log('lastname - ' + this.lastName)
    console.log('age - ' + this.age)
    console.log('heigtM - ' + this.heigtM)
    console.log('weightKg - ' + this.weightKg)
    console.log('Current Money - ' + this.getCash())
  }
}

const p = new Person('Ryu', 'Poolhopper', 40, 1.8, 140, new Wallet())
p.printState()

p.wallet.insertBill(5,3)
p.wallet.insertBill(100,2)

p.printState()
