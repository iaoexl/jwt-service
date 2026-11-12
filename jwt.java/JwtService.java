package com.jwt.test;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTCreator;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.Verification;

import javax.crypto.KeyGenerator;
import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.util.Date;

public class  JwtService {
    /**
     * 加密算法 可以抽象到环境变量中配置
     */
    private String MAC_NAME = "HMacSHA256";

    /**
     * 秘钥生成器
     */
    private KeyGenerator keyGenerator;

    /**
     * 加密算法
     */
    private static Algorithm algorithm;

    /**
     * 校验类
     */
    public static JWTVerifier jwtVerifier;

    /**
     * 校验器 用于生成 JWTVerifier 校验器
     */
    public static Verification verification;


    public void initAndRefresh(String dwmc) throws NoSuchAlgorithmException, UnsupportedEncodingException {


        algorithm = Algorithm.HMAC256(dwmc);
        verification = JWT.require(algorithm);
        jwtVerifier = verification.build();
    }

    public static String createToken(String dwdm, String dwmc) {

        JWTCreator.Builder builder = JWT.create();
        builder.withSubject(dwdm);
        builder.withIssuer(dwmc);
        builder.withExpiresAt(new Date(System.currentTimeMillis() + (24 * 3600 * 1000)));

String sign= builder.sign(algorithm);

        System.out.println(sign);
        return sign;
    }

// 测试环境
	public static void main(String[] args) throws Exception {
        JwtService jwtService = new JwtService();
		//单位名称
        jwtService.initAndRefresh("InstitutionName");
		//单位代码（YYYY-MM-DD+10位编号）+单位名称
        JwtService.createToken("202611120000000001", "InstitutionName");
		/** 有部分环境，要加个", 2"
		JwtService.createToken("202611120000000001", "InstitutionName", 2);
		**/
    } 
}