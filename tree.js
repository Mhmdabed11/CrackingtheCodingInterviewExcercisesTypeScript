class Node {
  constructor(val) {
    this.left = null;
    this.right = null;
    this.val = val;
  }
}

function insert(root, node) {
  if (!root) {
    root = node;
  }
  if (node.val > root.val) {
    if (!root.right) {
      root.right = node;
    } else {
      insert(root.right, node);
    }
  } else {
    if (!root.left) {
      root.left = node;
    } else {
      insert(root.left, node);
    }
  }
}

const root = new Node(3);
insert(root, new Node(1));
insert(root, new Node(10));
insert(root, new Node(13));
insert(root, new Node(8));
insert(root, new Node(9));
insert(root, new Node(2));

console.log(root);
