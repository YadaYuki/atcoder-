import * as readline from "readline";

class SegmentTree {
  private size: number;
  private size2pow: number; // size of array that managed by segment tree.
  private data: number[]; // array that represent segment tree.

  constructor(size: number, initialValue: number = 0) {
    // Initialize "size" by minimum power of 2 value bigger than "size"
    this.size = size;
    this.size2pow = 1;
    while (this.size2pow < size) {
      this.size2pow *= 2;
    }
    this.data = Array(this.size2pow * 2).fill(initialValue);
  }

  public getSize(): number {
    return this.size;
  }

  public update(
    idx: number, // min value of idx is 1.
    value: number
  ) {
    if (idx < 1 || this.size < idx) {
      throw Error(`idx is out of range. idx: ${idx}, size: ${this.size}`);
    }
    let nodeIdx = idx + (this.size2pow - 1);
    this.data[nodeIdx] = value;
    while (nodeIdx > 1) {
      nodeIdx = Math.floor(nodeIdx / 2);
      const leftChildNodeIdx = nodeIdx * 2;
      const rightChildNodeIdx = nodeIdx * 2 + 1;
      this.data[nodeIdx] = Math.max(
        this.data[leftChildNodeIdx],
        this.data[rightChildNodeIdx]
      );
    }
  }

  /*
   * return max value in [l,r)
   */
  public rmq(
    l: number, // min value of idx is 1.
    r: number
  ): number {
    const rmqRecursion = (
      l: number,
      r: number,
      currentL: number,
      currentR: number,
      nodeIdx: number
    ): number => {
      const isOut = r <= currentL || currentR <= l;
      const isIn = l <= currentL && currentR <= r;
      if (isOut) return -10000000000;
      if (isIn) return this.data[nodeIdx];
      const mid = Math.floor((currentL + currentR) / 2); //
      const rmqInLeft = rmqRecursion(l, r, currentL, mid, nodeIdx * 2);
      const rmqInRight = rmqRecursion(l, r, mid, currentR, nodeIdx * 2 + 1);
      return Math.max(rmqInLeft, rmqInRight);
    };
    return rmqRecursion(l, r, 1, this.size2pow + 1, 1);
  }
}

const main = () => {
  const lines: string[] = [];
  const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  reader.on("line", function (line) {
    lines.push(line);
  });

  reader.on("close", function () {
    const [N, Q] = lines[0].split(" ").map((val: string) => Number(val));
    const segTree = new SegmentTree(N);
    for (let i = 1; i <= Q; i++) {
      const query = lines[i].split(" ").map((val: string) => Number(val));
      const q = query[0];
      switch (q) {
        case 1:
          const [, pos, x] = query;
          segTree.update(pos, x);
          break;
        case 2:
          const [, l, r] = query;
          console.log(segTree.rmq(l, r));
          break;
      }
    }
  });

};

main();
