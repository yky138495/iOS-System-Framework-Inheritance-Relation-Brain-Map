//
//  CXAnswerCallAction.h
//  CallKit
//
//  Copyright © 2015 Apple. All rights reserved.
//

#import <CallKit/CXCallAction.h>

NS_ASSUME_NONNULL_BEGIN

CX_CLASS_AVAILABLE(ios(10.0))
@interface CXAnswerCallAction : CXCallAction

/// Normally, providers can just call -[CXAction fulfill] to indicate action fulfillment. Use this method to note a specific date that the call connected. A call is considered connected when both caller and callee can start communicating.
- (void)fulfillWithDateConnected:(NSDate *)dateConnected;

@end

NS_ASSUME_NONNULL_END
