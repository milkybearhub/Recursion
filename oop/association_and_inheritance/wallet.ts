export class Wallet {
    // public bill1: number
    // public bill5: number
    // public bill10: number
    // public bill20: number
    // public bill50: number
    // public bill100: number

    // constructor(
    //   bill1: number,
    //   bill5: number,
    //   bill10: number,
    //   bill20: number,
    //   bill50: number,
    //   bill100: number,  
    // ){
    //   this.bill1 = bill1
    //   this.bill5 = bill5
    //   this.bill10 = bill10
    //   this.bill20 = bill20
    //   this.bill50 = bill50
    //   this.bill100 = bill100
    // }

  // 上記は下記と同意
  // public も省略不可
  constructor(
    private bill1: number = 0,
    private bill5: number = 0,
    private bill10: number = 0,
    private bill20: number = 0,
    private bill50: number = 0,
    private bill100: number = 0,
  ){}

  getTotalMoney() {
    return (1*this.bill1) + (5*this.bill5) + (10*this.bill10) + (20*this.bill20) + (50*this.bill50) + (100*this.bill100)
  }

  insertBill(bill: number, amount: number) {
    switch (bill) {
      case 1:
        this.bill1 += amount
        break
      case 5:
        this.bill5 += amount
        break
      case 10:
        this.bill10 += amount
        break
      case 20:
        this.bill20 += amount
        break
      case 50:
        this.bill50 += amount
        break
      case 100:
        this.bill100 += amount
        break
      default:
        break
    }
  }
}
