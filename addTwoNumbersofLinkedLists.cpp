#include <bits/stdc++.h>

struct ListNode {
    int val;
    struct ListNode *next;
 };
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *p, *q, *t1, *t2;
    
    int carry = 0;
    int sum = 0;
    
    p = l1;
    q = l2;
    
    while(l1->next && l2->next){
        sum = l1->val + l2->val + carry;
        
        l1->val = sum % 10;
        l2->val = sum % 10;
        carry = sum / 10;
        
        l1 = l1->next;
        l2 = l2->next;
    }
    
    if(!l1->next && !l2->next)
    {
        sum = l1->val + l2->val + carry;
        
        l1->val = sum % 10;
        l2->val = sum % 10;
        carry = sum / 10;
        
        if(carry)
        {
            struct ListNode *new_node = (struct ListNode*) malloc(sizeof(struct ListNode));
            new_node->val = carry;
            new_node->next = NULL;
            
            l1->next = new_node;
        }
    }
        
    
    
    else if(!l2->next){
        sum = l1->val + l2->val + carry;
        
        l1->val = sum % 10;
        l2->val = sum % 10;
        
        carry = sum / 10;
        
        l1 = l1->next;
        while(l1)
        {
            sum = l1->val + carry;

            l1->val = sum % 10;
            carry = sum / 10;
            
            t1 = l1;
            l1 = l1->next; 
        }
        
        if(carry)
        {
            struct ListNode *new_node = (struct ListNode*) malloc(sizeof(struct ListNode));
            new_node->val = carry;
            new_node->next = NULL;
            
            t1->next = new_node;
        }
    }
    
    else if(!l1->next){
        sum = l1->val + l2->val + carry;
        
        l1->val = sum % 10;
        l2->val = sum % 10;
        
        carry = sum / 10;
        
        l2 = l2->next;
        while(l2)
        {
            sum = l2->val + carry;

            l2->val = sum % 10;
            carry = sum / 10;

            t2 = l2;
            l2 = l2->next; 
        }
        
        if(carry)
        {
            struct ListNode *new_node = (struct ListNode*) malloc(sizeof(struct ListNode));
            new_node->val = carry;
            new_node->next = NULL;
            
            t2->next = new_node;
        }
        
        return q;
    }
    
    return p;
}